
                  
# AKIRA-SYSYEM-SECURED-VAULT

# PROBLEM ???

In this current pandemic scenario most of the users are using their pcs to do their work and store important files related to their work, projects and accounts.
Even kids around age of 5-16years are downloading lots of important files through internet and exploring their world of education. 
we are unable to secure those  files and  folders. we don’t have any proper authenticated system to secure all those files. 

# example
If a 8 years kid using his father’s company laptop to play games, by accidentally if he delete any important files of project work it may cause large burden to his father 

# ARCHITECTURE
## In our project architecture, we divided this entire project into 2 parts. 
### NEW REGISTERATION PROCESS : 
During new user process when user enters to our application , firstly user needs to register in our application with their mail id through otp verification which is sent to the mail, and next to this user face id will be captured and stored in the system .
### REGISTERED USER PROCESS : 
In registered user process, User can login either by OTP verification or through face ID scan, if verification is done, user will be forwarded to primary page where they can lock/unlock the files.

# ARCHITECTURE OF NEW REGISTRATION PROCESS 

![image](https://drive.google.com/uc?export=view&id=1l3SIjEJ83i4HHWUu073OkavGJ9n4iBwZ)

During new registration process whenever the new user enters to our
application, firstly he/she needs to be register in our application by giving
his/her mail id and password by verifying their password twice. Whenever they
press submit button the mail otp page pops up then they need to place the otp
they received in the mail , it gone a verify the otp and let then user to scan
his/her face .The web cam will be turn on and user face id will be captured by
the system , and user face Id is also verified too. registration process will be
completed

# ARCHITECTURE OF REGISTERED USER 

![image](https://drive.google.com/uc?export=view&id=1B0iS6k3KXzIByRZ1acH7CQEu0s87AeLE)
After completing the registered user process will be taken, whenever user press
start button the registered user need to give either face id or mail otp. If anyone
of this is verified then he will be forward to our main application its primary
page where he can lock /unlock his files and folder .If the verification gets error
he will be forwared to error page which relocate back to starting page i.e. main
page of the project. Primary page has setting option also, where they can change
their face id, password, mail id. while changing user need to verify by giving
mail otp and old password.

# PROJECT COMPLETE ARCHITECTURE: 

![image](https://drive.google.com/uc?export=view&id=1N6GIMP_5YC9Nb67g04koFchjWZf_BGjR)

# AUTHENTICATION PROCESS:
## We divided the entire authentication process into 2 parts
### 1) Email-otp
### 2) Face lock

# 1.EMAIL-OTP AUTHENTICATION PROCESS:

In email-otp we have SMTP (system mail transfer protocol) it is an application
layer protocol, this library which help us to send mails from our server to user
mail server, and otp which is generated by system will encripte and saved in
system .so when user enter otp it will be encripted in system and check both
are same or not, if both are same let user to use if not pop up error message

![image](https://drive.google.com/uc?export=view&id=19oYIRxXOdIVBHhg7wJ8h3d0MyIdGSA-8)



2.FACE LOCK AUTHENTICATION PROCESS:

![image](https://drive.google.com/uc?export=view&id=1fWVbs4-7qbcwcNoiQK_sVZrS1nWrMNyP)
During new registration process the video will be captured from webcam and
splitting the images from captured video and prepares the dataset and sent for
pre-processing, feature extraction and classifiers helps the data set to classify
into known or unknown images, whenever the cv2 frame pop out it starts
recognizing face using face database if the user face is recognized 25 times or
more then will let user to access application.

# HASH ALGORITHM:
We used sha algorithm in our project, which has set of cryptography hash
functions defined by the language and we used this algorithm to convert the
information given by the user from string format to hash form
![image](https://drive.google.com/uc?export=view&id=1z_jAgqPrvwOyGX-Rd4rS20l2w6_U-zsp)

# CONCLUSION:
The conclusion of this project is We found some issues in the
existing folder locking system, such as when the user forgets the
password, then he/she was not able to retrieve the password.
Sometimes the locked folder can be deleted by the user accidentally
or intentionally. So, we have come up with an idea where users can
access the folder by using face-id or email-otp

# Used tech-
## python libraies
kivy,
kivymd,
random,
hashlib,
imutils ,
smtplib,
numpy, 
thinker,
pickle,
cv2,
os,
time,
sklearn.
## instruction to use 
install all pip libraies mentioned above and run main.py file 

# thank you
