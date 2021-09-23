# Deep-Learning-for-COVID19-Recognition-from-huge-X-Ray-dataset
This project makes use of Deep Learning to protrude COVID19 from 4 broad misleading diseases: Ground Glass Opacity, Viral Pneumonia, Corona and normal lung X-Rays.
The model is trained with VGG16 architecture and a sample set of around 20000 images. 
Kindly have a look at the evaluation metrics mentioned in the uploaded document. 
Also, this project has been successfully published on "SOLID STATE TECHNOLOGY" Journal (Volume 64, issue 2). However, the document is available to view in the repository.
Adding to this, I've also designed a simple flask aplication ready to get deployed on cloud platforms. Unfortunately, due to privacy concerns, I can't be putting its 
source code as it links my credentials for SMTP services. 
The trained model and requirements weigh around 1.1GB of storage which is not typically available for free on Heroku, GCP or even AWS. So I have turned that down.
You could view the GUI in the provided images though :)

Overview:
Host the application-> Python script loads Website-> User inputs image on website-> Python script predicts the severity using stored model(.H5)
->Predicted results are shown on site-> detailed classification is sent to user's mail ID

Thanks for reading :)
