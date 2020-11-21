from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import shutil
from kivymd.uix.taptargetview import MDTapTargetView
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import CircularRippleBehavior
from tkinter import messagebox,Tk,PhotoImage
from tkinter.filedialog import askopenfilename,askdirectory
from tkinter.messagebox import showinfo
import random
import hashlib
import playsound  # to play saved mp3 file
from gtts import gTTS
from imutils import paths
import smtplib
import numpy as np
import imutils
import pickle
import cv2
import os
from imutils.video import VideoStream
from imutils.video import FPS
import time
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
#MenuScreen:start button screen
#MenuScreen2: face and mail screen
#menu3 for setting
#ProfileScreen: locker
#ProfileScreen2: face scanner
#ProfileScreen3:otp enter security
#ProfileScreen4:face error(Please show your face to camera)
#ProfileScreen5: register page
#ProfileScreen6:password error
#ProfileScreen7:otp start up page
#ProfileScreen8:setting change password
#ProfileScreen8:setting change mail
#ProfileScreen10 face scan password
#UploadScreen:face  ACCESS DENIED
#UploadScreen2:otp error page
Window.size = (600, 600)
tpio = "gcjgcjc"
x = "en"
y = "hi"
num = 1
working=""
screen_helper = """
ScreenManager:
    id: screen_manager
    MenuScreen:
    MenuScreen2:
    MenuScreen3:
    ProfileScreen:
    ProfileScreen2:
    ProfileScreen3:
    ProfileScreen4:
    ProfileScreen5:
    ProfileScreen6:
    ProfileScreen7:
    ProfileScreen8:
    ProfileScreen9:
    ProfileScreen10
    UploadScreen:
    UploadScreen2:
<MenuScreen>:
    id: scr_io
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5

        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    CircularRippleButton:
        source: f"output/icon.png"
        size_hint: None, None
        size: "400dp", "400dp"
        pos_hint: {"center_x":.5, "center_y":.6}
    MDFillRoundFlatIconButton:
        text: "start"
        icon:'fire'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.test()
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                title: ''
                id:button
                icon: 'home'
                type: 'bottom'
<MenuScreen3>:
    id: scr_io
    name: 'menu3'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5

        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    CircularRippleButton:
        source: f"output/icon.png"
        size_hint: None, None
        size: "200dp", "200dp"
        pos_hint: {"center_x":.5, "center_y":.7}
    MDFillRoundFlatIconButton:
        text: "change face ID"
        icon:'face'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'profile10'
    MDFillRoundFlatIconButton:
        text: "change password"
        icon:'text'
        pos_hint: {'center_x':0.5,'center_y':0.35}
        on_press: root.manager.current = 'profile8'
    MDFillRoundFlatIconButton:
        text: "change mail"
        icon:'mail'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'profile9'
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                title: ''
                id:button
                on_action_button:root.manager.current = 'menu'
                icon: 'home'
                type: 'bottom'
<MenuScreen2>:
    id: scr_io
    name: 'menu2'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5

        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    CircularRippleButton:
        source: f"output/icon.png"
        size_hint: None, None
        size: "200dp", "200dp"
        pos_hint: {"center_x":.5, "center_y":.7}
    MDFillRoundFlatIconButton:
        text: "Face Lock"
        icon:'face'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.git()
    MDFillRoundFlatIconButton:
        text: "email otp"
        icon:'mail'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press:root.mail()
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                title: ''
                id:button
                icon: 'lock'
                type: 'bottom'



<ProfileScreen>:
    name: 'profile'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5

        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    CircularRippleButton:
        source: f"output/icon.png"
        size_hint: None, None
        size: "200dp", "200dp"
        pos_hint: {"center_x":.5, "center_y":.7}
    MDFillRoundFlatIconButton:
        text: "drop file(img,docx,..)"
        icon:'file'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.Brow()
    MDFillRoundFlatIconButton:
        text: "drop floder"
        icon:'folder'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.Brow2()
    MDFillRoundFlatIconButton:
        text: "Lock/Unlock"
        icon:'lock'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press:root.kick()
    MDFloatingActionButton:
        text: ""
        icon:'settings'
        pos_hint: {'center_x':0.1,'center_y':0.15}
        on_press:root.manager.current = 'menu3'
            
    MDBottomAppBar:
        MDToolbar:
            title: ''
            id:button
            icon: 'lock'
            type: 'bottom'
            on_action_button: root.tap_target_start()
            
<ProfileScreen3>:
    name: 'profile3'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    MDLabel:
        text: 'OTP'
        pos_hint: {'x':0.3,'y':0.09}
    MDTextFieldRect:
        size_hint:.4,.10
        hint_text: "OTP"
        id:my_input
        pos_hint: {'center_x':0.5,'center_y':0.5}
        normal_color: app.theme_cls.accent_color
    MDFillRoundFlatIconButton:
        text: "submit"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press:root.bit()
  
    MDBottomAppBar:
        MDToolbar:
            title: ''
            id:button
            on_action_button: root.manager.current = 'menu'
            icon: 'home'
            type: 'bottom'
<ProfileScreen7>:
    name: 'profile7'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    MDLabel:
        text: 'OTP'
        pos_hint: {'x':0.3,'y':0.09}
    MDTextFieldRect:
        size_hint:.4,.10
        hint_text: "OTP"
        id:my_input
        pos_hint: {'center_x':0.5,'center_y':0.5}
        normal_color: app.theme_cls.accent_color
    MDFillRoundFlatIconButton:
        text: "submit"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press:root.bit()
  
    MDBottomAppBar:
        MDToolbar:
            title: ''
            id:button
            on_action_button: root.manager.current = 'profile5'
            icon: 'home'
            type: 'bottom'
<ProfileScreen5>:
    name: 'profile5'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    MDLabel:
        text: 'mail ID'
        pos_hint: {'x':0.45,'y':0.3}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "mail"
        id:my_input
        pos_hint: {'center_x':0.5,'center_y':0.75}
        normal_color: app.theme_cls.accent_color
    MDLabel:
        text: 'new password'
        pos_hint: {'x':0.4,'y':0.15}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "password"
        id:my_input2
        pos_hint: {'center_x':0.5,'center_y':0.6}
        normal_color: app.theme_cls.accent_color
    MDLabel:
        text: 'conform password'
        pos_hint: {'x':0.4,'y':0.0}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "password"
        id:my_input3
        pos_hint: {'center_x':0.5,'center_y':0.45}
        normal_color: app.theme_cls.accent_color
    MDFillRoundFlatIconButton:
        text: "submit"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press:root.bit()
  
    MDBottomAppBar:
        MDToolbar:
            title: ''
            id:button
            on_action_button: root.manager.current = 'menu'
            icon: 'home'
            type: 'bottom'
<ProfileScreen8>:
    name: 'profile8'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    MDLabel:
        text: 'old password'
        pos_hint: {'x':0.45,'y':0.3}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "password"
        id:my_input
        pos_hint: {'center_x':0.5,'center_y':0.75}
        normal_color: app.theme_cls.accent_color
    MDLabel:
        text: 'new password'
        pos_hint: {'x':0.4,'y':0.15}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "password"
        id:my_input2
        pos_hint: {'center_x':0.5,'center_y':0.6}
        normal_color: app.theme_cls.accent_color
    MDLabel:
        text: 'conform password'
        pos_hint: {'x':0.4,'y':0.0}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "password"
        id:my_input3
        pos_hint: {'center_x':0.5,'center_y':0.45}
        normal_color: app.theme_cls.accent_color
    MDFillRoundFlatIconButton:
        text: "submit"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press:root.bit()
    MDBottomAppBar:
        MDToolbar:
            title: ''
            id:button
            on_action_button: root.manager.current = 'menu'
            icon: 'home'
            type: 'bottom'
<ProfileScreen9>:
    name: 'profile9'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    MDLabel:
        text: 'password'
        pos_hint: {'x':0.45,'y':0.3}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "password"
        id:my_input
        pos_hint: {'center_x':0.5,'center_y':0.75}
        normal_color: app.theme_cls.accent_color
    MDLabel:
        text: 'Mail'
        pos_hint: {'x':0.4,'y':0.15}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "Mail"
        id:my_input2
        pos_hint: {'center_x':0.5,'center_y':0.6}
        normal_color: app.theme_cls.accent_color
    MDLabel:
        text: 'Conform Mail'
        pos_hint: {'x':0.4,'y':0.0}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "Mail"
        id:my_input3
        pos_hint: {'center_x':0.5,'center_y':0.45}
        normal_color: app.theme_cls.accent_color
    MDFillRoundFlatIconButton:
        text: "submit"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press:root.bit()
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                title: ''
                id:button
                on_action_button:root.manager.current = 'menu'
                icon: 'home'
                type: 'bottom'
<ProfileScreen10>:
    name: 'profile10'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    MDLabel:
        text: 'password'
        pos_hint: {'x':0.45,'y':0.5}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "password"
        id:my_input
        pos_hint: {'center_x':0.5,'center_y':0.75}
        normal_color: app.theme_cls.accent_color
    MDFillRoundFlatIconButton:
        text: "submit"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press:root.bit()
  
    MDBottomAppBar:
        MDToolbar:
            title: ''
            id:button
            on_action_button: root.manager.current = 'menu'
            icon: 'home'
            type: 'bottom'

<ProfileScreen4>:
    name: 'profile4'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    
    CircularRippleButton:
        source: f"output/sad3.png"
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
    MDLabel:
        text: 'ERROR'
        theme_text_color: "Error"
        halign: "center"
        pos_hint: {'x':0.0,'y':-.3}
    MDLabel:
        text: 'Please show your face to camera'
        halign: "center"
        pos_hint: {'x':-0.0,'y':-.33}
      
    MDFillRoundFlatIconButton:
        text: "scan again"
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:root.manager.current = 'profile2'
<ProfileScreen2>:
    name: 'profile2'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    
    CircularRippleButton:
        source: f"output/ip5.png"
        size_hint: None, None
        size: "600dp", "300dp"
        pos_hint: {"center_x": .5, "center_y": .5} 
    MDLabel:
        text: 'please avoid too much lighting in back ground'
        halign: "center"
        pos_hint: {'x':-0.0,'y':-.33}  
    MDFillRoundFlatIconButton:
        text: "SCAN"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:root.first() 
<ProfileScreen6>:
    name: 'profile6'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    
    CircularRippleButton:
        source: f"output/sad3.png"
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
    MDLabel:
        text: 'ERROR'
        theme_text_color: "Error"
        halign: "center"
        pos_hint: {'x':0.0,'y':-.3}
    MDLabel:
        text: 'Please check your password try again'
        halign: "center"
        pos_hint: {'x':-0.0,'y':-.33}
      
    MDFillRoundFlatIconButton:
        text: "try again"
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:root.manager.current = 'menu'
<ProfileScreen2>:
    name: 'profile2'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    
    CircularRippleButton:
        source: f"output/ip5.png"
        size_hint: None, None
        size: "600dp", "300dp"
        pos_hint: {"center_x": .5, "center_y": .5} 
    MDLabel:
        text: 'please avoid too much lighting in back ground'
        halign: "center"
        pos_hint: {'x':-0.0,'y':-.33}  
    MDFillRoundFlatIconButton:
        text: "SCAN"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:root.first() 
    
<UploadScreen>:
    name: 'upload'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    
    CircularRippleButton:
        source: f"output/sad3.png"
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
    MDLabel:
        text: 'ACCESS DENIED'
        theme_text_color: "Error"
        halign: "center"
        pos_hint: {'x':0.0,'y':-.3}
    MDLabel:
        text: 'some  times  it  occur due to less light. so  please try mail otp'
        halign: "center"
        pos_hint: {'x':-0.0,'y':-.33}
      
    MDFillRoundFlatIconButton:
        text: "Home"
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:root.manager.current = 'menu'

<UploadScreen2>:
    name: 'upload2'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'AK-SYSTEM SECURITY'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    
    CircularRippleButton:
        source: f"output/sad3.png"
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
    MDLabel:
        text: 'ACCESS DENIED'
        theme_text_color: "Error"
        halign: "center"
        pos_hint: {'x':0.0,'y':-.3}
    MDLabel:
        text: ' please try with valid otp'
        halign: "center"
        pos_hint: {'x':-0.0,'y':-.33}
      
    MDFillRoundFlatIconButton:
        text: "Home"
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:root.manager.current = 'menu'

"""

class MenuScreen(Screen):

    def test(self):
        try:
            os.chdir(working)
        except:
            pass
        if os.path.exists("output/password.txt"):
            self.manager.current = "menu2"
        else:
            self.manager.current="profile5"
class MenuScreen3(Screen):
    def test(self):
        self.manager.current="profile2"
class MenuScreen2(Screen):

    def mail(self):
        try:
            pop=random.randint(1000,9999)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("Facemaskdetector@gmail.com", "majorproject")
            SUBJECT = "otp ak locker"+str(pop)
            TEXT = str(pop)
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            file=open("output/mail.txt","r")
            mail=file.read()
            file.close()
            s.sendmail("Facemaskdetector@gmail.com",mail, message)
            s.quit()
            file=open("output/otp.txt",'w')
            result = hashlib.sha256(str(pop).encode())
            file.write(result.hexdigest())
            file.close()
            print("sucessfull")
            self.manager.current = "profile3"
        except:
            print("wifi issue")

    def navigation_draw(self):
        sender = 'from@fromdomain.com'
        receivers = ['to@todomain.com']

        message = """From: From Person <from@fromdomain.com>
        To: To Person <to@todomain.com>
        Subject: SMTP e-mail test

        This is a test e-mail message.
        """

        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail(sender, receivers, message)
            print("Successfully sent email")
        except:
            print("Error: unable to send email")

    def git2(self):
        self.manager.current="profile2"
        return


    def git(self):
     stop =""
     if os.path.exists("output/recognizer.pickle"):
         print("yes")
     else:
         pass
     try:
         print("hi")
         print("[INFO] loading face detector...")

         detector = cv2.dnn.readNetFromCaffe('output/deploy.prototxt',
                                             'output/res10_300x300_ssd_iter_140000.caffemodel')

         print("[INFO] loading face recognizer...")
         embedder = cv2.dnn.readNetFromTorch("output/openface_nn4.small2.v1.t7")

         recognizer = pickle.loads(open("output/recognizer.pickle", "rb").read())
         le = pickle.loads(open("output/le.pickle", "rb").read())

         print("[INFO] starting video stream...")
         vs = VideoStream(src=0).start()
         time.sleep(2.0)
         fps = FPS().start()
         lio = 0
         tio=0
         while True:
             frame = vs.read()
             frame = imutils.resize(frame, width=600)
             (h, w) = frame.shape[:2]

             imageBlob = cv2.dnn.blobFromImage(
                 cv2.resize(frame, (300, 300)), 1.0, (300, 300),
                 (104.0, 177.0, 123.0), swapRB=False, crop=False)

             detector.setInput(imageBlob)
             detections = detector.forward()

             for i in range(0, detections.shape[2]):

                 confidence = detections[0, 0, i, 2]

                 if confidence > 0.5:

                     box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                     (startX, startY, endX, endY) = box.astype("int")

                     # extract the face ROI
                     face = frame[startY:endY, startX:endX]
                     (fH, fW) = face.shape[:2]

                     if fW < 20 or fH < 20:
                         continue

                     faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                                      (96, 96), (0, 0, 0), swapRB=True, crop=False)
                     embedder.setInput(faceBlob)
                     vec = embedder.forward()

                     preds = recognizer.predict_proba(vec)[0]
                     j = np.argmax(preds)
                     proba = preds[j]
                     name = le.classes_[j]
                     print(name)
                     lk = proba * 100
                     print(lk)
                     lk2 = name
                     if lk > 50 and lk2 == "sai":
                         lio = lio + 1
                         print(lio)
                     if lio > 15:
                         print("acess granted")
                         stop = "stop"
                         self.manager.current = "profile"

                     if lk > 50 and lk2 == "unknown":
                         tio = tio + 1
                         print(tio)
                     if tio > 25:
                         print("acess denied")
                         stop = "stop2"
                         self.manager.current = "upload"




                     text = "{}: {:.2f}%".format(name, proba * 100)
                     y = startY - 10 if startY - 10 > 10 else startY + 10
                     cv2.rectangle(frame, (startX, startY), (endX, endY),
                                   (0,255,0), 2)

             fps.update()

             cv2.imshow("Frame", frame)
             key = cv2.waitKey(1) & 0xFF
             if stop == "stop":
                 break
             if stop == "stop2":
                 break

         fps.stop()
         print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
         print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
         cv2.destroyAllWindows()
         vs.stop()
         if stop == "stop":
             print("access granted")



         if stop == "stop2":
             print("access denied")

     except:

         self.manager.current="profile2"
class ProfileScreen(Screen):
    def Brow(self):
        window = Tk()
        try:
            os.chdir(working)
            shutil.move(os.path.join(os.path.expandvars("%userprofile%"), "Desktop" + "/Locker"),
                        os.getcwd() + "/output/public/")
        except:
            pass
        try:
            os.chdir("output/public/")
        except:
            pass
        window.withdraw()
        try:
            dwldDirectory = askopenfilename()
            try:
                os.chdir("output/public/")
                os.remove("unlock.bat")
                os.remove("unlock.txt")
            except:
                pass
            print(os.getcwd())
            fob = open('unlock.txt', 'w')
            fob.write("@ECHO OFF\n"
                      "attrib -h -s "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"\n'
                      "ren "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"'" Locker\n"
                      "echo Folder Unlocked successfully\n"
                      "goto End\n"
                      ":End")
            fob.close()
            os.rename("unlock.txt", "unlock.bat")
            os.startfile("unlock.bat")
            time.sleep(1)
            if os.path.exists("Locker"):
                print("remove")
                os.remove("unlock.bat")
            try:
                shutil.move(dwldDirectory, "Locker/locked files/")
                time.sleep(1)
                fob = open('lock.txt', 'w')
                fob.write("@ECHO OFF\n"
                          "ren Locker "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"\n'
                          "attrib +h +s "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"\n'
                          "echo Folder locked\n"
                          "goto End\n"
                          ":End\n")
                fob.close()
                os.rename("lock.txt", "lock.bat")
                os.startfile("lock.bat")
                time.sleep(1)
                os.remove("lock.bat")
                print("work done")
                try:
                    os.remove("unlock.bat")
                except:
                    pass
                messagebox.showinfo("SUCCESS", "file safely stored in locker")
            except:
                messagebox.showinfo("error",
                                    "unable to export file do it manually or same name file already exist in locker folder)")
                self.lock()
            window.destroy()
        except:
            showinfo("error", "please select the file or same name file already exist in locker folder)")
            print(os.getcwd())
            self.lock()
            pass
    def unlock(self):
        try:
            os.chdir("output/public")
        except:
            pass
        print(os.getcwd())
        fob = open('unlock.txt', 'w')
        fob.write("@ECHO OFF\n"
                  "attrib -h -s "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"\n'
                  "ren "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"'" Locker\n"
                  "echo Folder Unlocked successfully\n"
                  "goto End\n"
                  ":End")
        fob.close()
        os.rename("unlock.txt", "unlock.bat")
        os.startfile("unlock.bat")
        time.sleep(1)
        if os.path.exists("Locker"):
            print("remove")
            os.remove("unlock.bat")
            shutil.move("Locker",os.path.join(os.path.expandvars("%userprofile%"),"Desktop"))
            time.sleep(1)
            os.startfile(os.path.join(os.path.expandvars("%userprofile%"), "Desktop"+"/Locker"))
    def kick(self):
        if os.path.exists("output/public/Locker"):
            print("loker")
            self.lock()
        elif os.path.exists(os.path.join(os.path.expandvars("%userprofile%"), "Desktop"+"/Locker")):
            print("locker")
            self.lock()
        else:
            self.unlock()
            print("unlock")
    def lock(self):
        try:
            os.chdir("output/public")
        except:
            pass
        try:
            shutil.move(os.path.join(os.path.expandvars("%userprofile%"), "Desktop"+"/Locker"),os.getcwd())
        except:
            pass
        fob = open('lock.txt', 'w')
        fob.write("@ECHO OFF\n"
                  "ren Locker "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"\n'
                  "attrib +h +s "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"\n'
                  "echo Folder locked\n"
                  "goto End\n"
                  ":End\n")
        fob.close()
        os.rename("lock.txt", "lock.bat")
        os.startfile("lock.bat")
        time.sleep(1)
        os.remove("lock.bat")
        print("work done")
    def Brow2(self):
        window = Tk()
        try:
            os.chdir(working)
            shutil.move(os.path.join(os.path.expandvars("%userprofile%"), "Desktop"+"/Locker"),os.getcwd()+"/output/public/")
        except:
            pass
        try:
            os.chdir("output/public/")
        except:
            pass
        window.withdraw()
        try:
            dwldDirectory = askdirectory()
            try:
                os.chdir("output/public/")
                os.remove("unlock.bat")
                os.remove("unlock.txt")
            except:
                pass
            print(os.getcwd())
            fob = open('unlock.txt', 'w')
            fob.write("@ECHO OFF\n"
                      "attrib -h -s "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"\n'
                      "ren "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"'" Locker\n"
                      "echo Folder Unlocked successfully\n"
                      "goto End\n"
                      ":End")
            fob.close()
            os.rename("unlock.txt", "unlock.bat")
            os.startfile("unlock.bat")
            time.sleep(1)
            if os.path.exists("Locker"):
                print("remove")
                os.remove("unlock.bat")
            try:
                shutil.move(dwldDirectory, "Locker/locked folders/")
                time.sleep(1)
                fob = open('lock.txt', 'w')
                fob.write("@ECHO OFF\n"
                          "ren Locker "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"\n'
                          "attrib +h +s "'"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"\n'
                          "echo Folder locked\n"
                          "goto End\n"
                          ":End\n")
                fob.close()
                os.rename("lock.txt", "lock.bat")
                os.startfile("lock.bat")
                time.sleep(1)
                os.remove("lock.bat")
                print("work done")
                try:
                    os.remove("unlock.bat")
                except:
                    pass
                messagebox.showinfo("SUCCESS", "file safely stored in locker")
            except:
                messagebox.showinfo("error", "unable to export file do it manually or same name file already exist in locker folder)")
                self.lock()
            window.destroy()
        except:
            showinfo("error", "please select the file or same name file already exist in locker folder)")
            print(os.getcwd())
            self.lock()
            pass
    def tap_target_start(self):
        self.tap_target_view = MDTapTargetView(
            widget=self.ids['button'],
            title_text="akria",
            description_text="what can i do for you sir?",
            widget_position="center",
            title_position="left_top",
            outer_radius=150,
        )
        if self.tap_target_view.state == "open":
            self.tap_target_view.stop()
        else:
            self.tap_target_view.start()
class ProfileScreen3(Screen):
    def bit(self):
        lol=self.ids['my_input'].text
        lk=hashlib.sha256(str(lol).encode())
        file=open("output/otp.txt","r")
        r=file.read()
        file.close()
        if lol=="":
            self.manager.current = "upload2"
        else:
            if lk.hexdigest()==r:
                self.manager.current = "profile"
            else:
                self.manager.current = "upload2"
class ProfileScreen7(Screen):
    def bit(self):
        print("ko")
        lol=self.ids['my_input'].text
        lk=hashlib.sha256(str(lol).encode())
        file=open("output/otp.txt","r")
        r=file.read()
        file.close()
        if lol=="":
            self.manager.current = "upload2"
        else:
            if lk.hexdigest()==r:
                self.manager.current = "profile2"
            else:
                os.remove("output/mail.txt")
                os.remove("output/password.txt")
                self.manager.current = "upload2"
class ProfileScreen5(Screen):
    def bit(self):
        lol3=lol=self.ids['my_input3'].text
        lol=self.ids['my_input'].text
        lol2= self.ids['my_input2'].text
        if lol2==lol3:
            lk = hashlib.sha256(str(lol2).encode())
            file = open("output/mail.txt", "w")
            file.write(lol)
            file.close()
            file2 = open("output/password.txt", "w")
            file2.write(str(lk.hexdigest()))
            file2.close()
            try:
                print("hi")
                pop = random.randint(1000, 9999)
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("Facemaskdetector@gmail.com", "majorproject")
                SUBJECT = "otp ak locker" + str(pop)
                TEXT = str(pop)
                message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                file = open("output/mail.txt", "r")
                mail = file.read()
                file.close()
                s.sendmail("Facemaskdetector@gmail.com", mail, message)
                s.quit()
                file = open("output/otp.txt", 'w')
                result = hashlib.sha256(str(pop).encode())
                file.write(result.hexdigest())
                file.close()
                print("sucessfull")
                os.mkdir("output/public")
                os.wait(1)
                os.mkdir("output/public/locker")
                self.manager.current = "profile3"
            except:
                print("wifi issue")
            self.manager.current = "profile7"
        else:
            self.manager.current="profile6"
class ProfileScreen8(Screen):
    def bit(self):
        os.chdir(working)
        lol3=self.ids['my_input3'].text
        lol=self.ids['my_input'].text
        lol2= self.ids['my_input2'].text
        if lol2==lol3:
            lk = hashlib.sha256(str(lol2).encode())
            lk2 = hashlib.sha256(str(lol).encode())
            file=open("output/password.txt")
            password=file.read()
            file.close()
            if lk2.hexdigest()==password:
                file2 = open("output/password.txt", "w")
                file2.write(str(lk.hexdigest()))
                file2.close()
                self.manager.current="menu"
            else:
                self.manager.current="profile6"
class ProfileScreen9(Screen):
    def bit(self):
        os.chdir(working)
        lol3=self.ids['my_input3'].text
        lol=self.ids['my_input'].text
        lol2= self.ids['my_input2'].text
        if lol2==lol3:
            lk2 = hashlib.sha256(str(lol).encode())
            file=open("output/password.txt")
            password=file.read()
            file.close()
            if lk2.hexdigest()==password:
                file2 = open("output/mail.txt", "w")
                file2.write(str(lol2))
                file2.close()
                self.manager.current="menu"
            else:
                self.manager.current="profile6"
class ProfileScreen10(Screen):
    def bit(self):
        os.chdir(working)
        lol=self.ids['my_input'].text
        lk2 = hashlib.sha256(str(lol).encode())
        file=open("output/password.txt")
        password=file.read()
        file.close()
        if lk2.hexdigest()==password:
            self.manager.current="profile2"
        else:
            self.manager.current="profile6"
class ProfileScreen4(Screen):

    def ext(self):
        print("hi")
class ProfileScreen6(Screen):

    def ext(self):
        print("hi")
class ProfileScreen2(Screen):

    def ext(self):

        print("[INFO] loading face detector...")
        detector = cv2.dnn.readNetFromCaffe('output/deploy.prototxt',
                                            'output/res10_300x300_ssd_iter_140000.caffemodel')

        print("[INFO] loading face recognizer...")
        embedder = cv2.dnn.readNetFromTorch("output/openface_nn4.small2.v1.t7")

        print("[INFO] quantifying faces...")
        imagePaths = list(paths.list_images("dataset"))
        knownEmbeddings = []
        knownNames = []
        total = 0
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            print("[INFO] processing image {}/{}".format(i + 1,
                                                         len(imagePaths)))
            name = imagePath.split(os.path.sep)[-2]
            image = cv2.imread(imagePath)
            image = imutils.resize(image, width=600)
            (h, w) = image.shape[:2]
            imageBlob = cv2.dnn.blobFromImage(
                cv2.resize(image, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)
            detector.setInput(imageBlob)
            detections = detector.forward()
            if len(detections) > 0:
                i = np.argmax(detections[0, 0, :, 2])
                confidence = detections[0, 0, i, 2]
                if confidence > 0.5:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    face = image[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]
                    if fW < 20 or fH < 20:
                        continue
                    faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                                     (96, 96), (0, 0, 0), swapRB=True, crop=False)
                    embedder.setInput(faceBlob)
                    vec = embedder.forward()
                    knownNames.append(name)
                    knownEmbeddings.append(vec.flatten())
                    total += 1
        print("[INFO] serializing {} encodings...".format(total))
        data = {"embeddings": knownEmbeddings, "names": knownNames}
        f = open("output/embeddings.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()
    def train(self):
        print("[INFO] loading face embeddings...")
        data = pickle.loads(open("output/embeddings.pickle", "rb").read())
        print("[INFO] encoding labels...")
        le = LabelEncoder()
        labels = le.fit_transform(data["names"])
        print("[INFO] training model...")
        recognizer = SVC(C=1.0, kernel="linear", probability=True)
        recognizer.fit(data["embeddings"], labels)
        f = open("output/recognizer.pickle", "wb")
        f.write(pickle.dumps(recognizer))
        f.close()
        f = open("output/le.pickle", "wb")
        f.write(pickle.dumps(le))
        f.close()
        print("work done")
    def pic(self):
        faceCascade = cv2.CascadeClassifier("output/haarcascade_frontalface_default.xml")

        video_capture = cv2.VideoCapture(0)
        currentframe = 0
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)
            if ret:
                name = './dataset/sai/' + str(currentframe) + '.jpg'
                print('Creating...' + name)
                cv2.imwrite(name, frame)
                currentframe += 1
                if currentframe == 25:
                    break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()

    def first(self):
        try:
            self.pic()
            self.ext()
            self.train()
            self.manager.current="menu"
        except:
            self.manager.current="profile4"

    def first5(self):
        print("hi")
    pass
class UploadScreen(Screen):
    def capture(self):
        print("hi")
    # pytessercat
class UploadScreen2(Screen):
    def capture(self):
        print("hi")
# the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MenuScreen2(name='menu2'))
sm.add_widget(MenuScreen2(name='menu3'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(ProfileScreen3(name='profile3'))
sm.add_widget(ProfileScreen4(name='profile4'))
sm.add_widget(ProfileScreen5(name='profile5'))
sm.add_widget(ProfileScreen2(name='profile2'))
sm.add_widget(ProfileScreen2(name='profile6'))
sm.add_widget(ProfileScreen2(name='profile7'))
sm.add_widget(ProfileScreen2(name='profile8'))
sm.add_widget(ProfileScreen2(name='profile9'))
sm.add_widget(ProfileScreen10(name='profile10'))
sm.add_widget(UploadScreen(name='upload'))
sm.add_widget(UploadScreen(name='upload2'))
class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 0.85
        super().__init__(**kwargs)
class AkApp(MDApp):
    def build(self):
        print(os.getcwd())
        global working
        working=os.getcwd()
        self.theme_cls.primary_palette = "Blue"
        screen = Builder.load_string(screen_helper)
        return screen
AkApp().run()