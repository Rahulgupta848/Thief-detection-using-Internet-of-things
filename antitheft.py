import sys
import RPi.GPIO as GPIO
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
import cv2 

BUTTON_GPIO=19
pir=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)
pwm=GPIO.PWM(3,50)
pwm.start(0)

def mails(count):
    count=str(count)
    fromaddr = "rg547726@gmail.com"
    password='rahul123'
    toaddr = 'rsgupta848@gmail.com'
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    # storing the subject 
    msg['Subject'] = "RBC  count"
    # string to store the body of the mail 
    body = count
    msg.attach(MIMEText(body, 'plain'))
    filename='1.jpg'
    filename = filename 
    attachment = open(filename, "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login(fromaddr, password) 
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 



GPIO.add_event_detect(i1, GPIO.RISING, callback=my_callback1, bouncetime=300)

    
def SetAngle(angle):
    duty=angle/18+2
    GPIO.output(3,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3,False)
    pwm.ChangeDutyCycle(0)
def button_pressed_callback(channel):
    print("gate open")
    SetAngle(90)
    sleep(2)
    SetAngle(0)
def capture(channel):
    print("person detected")
    cam=cv2.VideoCapture('http://192.168.0.104:8081')
    ret,image=cam.read()
    if ret:
        cv2.imwrite('1.jpg',image)
    cam.release()
    mails('http://192.168.0.104/home')
print('ok')
GPIO.setup(BUTTON_GPIO,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(pir,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTON_GPIO,GPIO.FALLING,callback=button_pressed_callback,bouncetime=100)
GPIO.add_event_detect(pir,GPIO.FALLING,callback=capture,bouncetime=100)
        
         
