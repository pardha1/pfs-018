#email with multiple users with attachments:

import smtplib #simple mail transfer protocol lib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase
from email import encoders #binary code-bytes 8,32,64
import os # to check the paths avaialble or not?


username="likhitasowmya567@gmail.com"
password="ekzggtjinmogrvmf"


def send_mail(to,subject,body,attachement):
    try:
        msg=MIMEMultipart()
        msg["from"]=username
        msg["to"]=to
        msg["subject"]=subject
        msg.attach(MIMEText(body,"plain"))

        #attachements:
        for path in attachement:
            if path and os.path.exists(path):
                with open (path,"rb") as f:#rb read binary
                    part=MIMEBase("application","octet-stream")       #(type,subtype)
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    msg.add_header("a",f'{os.path.basename(path)}')
                    msg.attach(part)
            else:
                print("path not found")
                    
        #server:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls() #transfer layer security

        server.login(username,password)

        server.sendmail(username,to,subject,msg.as_string())

        print(f"mail sent succefully to {to}")
        

    except Exception as e:
        print(e)

too=input("enter mail sep with,:")
to=[i for i in too.split(",")]

subject=input("enter subject:")
body=input("enter body:")

p=input("enter paths sep with ,:")
attachement=[i for i in p.split(",")]

for i in to:
    send_mail(i,subject,body,attachement)

        
    
