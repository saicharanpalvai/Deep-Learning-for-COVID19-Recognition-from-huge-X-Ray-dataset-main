import flask
import pandas as pd
import smtplib
import base64
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import json

import numpy as np

def getOutput(stri):
  img= image.load_img("temp.jpeg", target_size=(299,299))
  img=np.asarray(img)
  img=np.expand_dims(img,axis=0)
  saved_model=load_model('model/SaveState3.h5')
  output=saved_model.predict(img)
  return output

app = flask.Flask(__name__, template_folder='templates')
@app.route('/',methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))
    if flask.request.method == 'POST':
        mail=flask.request.form.getlist('mailid')
        print(mail)
        uploaded_file = flask.request.files['file']
        if uploaded_file.filename != '':
            namefile="temp.jpeg"
            uploaded_file.save(namefile)
            output=getOutput("temp.jpeg");
            maxi=0
            for i in range(4):
              if(output[0][i]>output[0][maxi]):
                maxi=i
            diction = {0:'Diagnosed with COVID-19!', 1:'Diagnosed with Ground Glass Opacity!', 2: 'Healthy', 3: 'Diagnosed with Viral Pneumonia!'}
            prediction=diction[maxi]
        filename = "temp.jpeg"
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "miniproj1234@gmail.com"  # Enter your address
        receiver_email = mail[0]  # Enter receiver address
        password = "########"
        s2=prediction
        s="\nClass Probabilities are: \n[COVID19:"+str(output[0][0])+" Ground_Glass_Opacity:"+str(output[0][1])+" Normal:"+str(output[0][2])+" Viral_Pneumonia:"+str(output[0][3])+"]\n"
        body = "Dear user, \n\tBased on the symptoms marked and the chest X-Ray uploaded, our Deep Learning model has predicted the following:\n "+ s+s2
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        subject = "Radiography based Diagnosis of COVID-19 using Deep Learning"
        message["Subject"] = subject
        message["Bcc"] = "nikhil.madhavaneni@gmail.com"
        message.attach(MIMEText(body, "plain"))
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        message.attach(part)
        text = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        return flask.render_template('main.html',result=prediction)

if __name__ == '__main__':
    app.run()
