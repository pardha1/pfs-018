import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#username="akhilathotakura3@gmail.com"
username="pardhu4563@gmail.com"
password="ntlo uskz rwlq foij"
#password="xqculhhwnlurtdor"

def send_mail(to,subject,body):
    try:
        msg=MIMEMultipart()
        msg["from"]=username
        msg["to"]=to
        msg["subject"]=subject
        msg.attach(MIMEText(body,"plain"))
#server:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(username,password)
        server.sendmail(username,to,msg.as_string())
        print(f"mail sent succefully to {to}")

        server.quit()
    except Exception as e:
        print(f"{error},e")

too=input("enter mail id #seperate with ,")
sending=[i for i in too.split(",")]

subject=input("enter subject:")
body=input("enter matter:")

for email in sending:
    send_mail(email,subject,body)

    

