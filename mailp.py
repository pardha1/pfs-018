##import smtplib
##try:
##    username="pardhu4563@gmail.com"
##    password="ntlo uskz rwlq foij"
##    
##    s=smtplib.SMTP("smtp.gmail.com",587)
##    s.starttls()
##    
##    receiver="tanarapuchakrapani9491@gmail.com"
##    
##    s.login(username,password)
##    
##    msg="hii i am sending mail using python"
##
##    s.sendmail(username,receiver,msg)
##    print("mail sent")
##
##except Exception as e:
##    print(e)
##
##


#email:
'''

import smtplib
import random
import string

otp=""
for i in range(3):
    otp+=str(random.randint(1,9))
for j in range(3):
    otp+=random.choice(string.ascii_letters)

l_otp=list(otp)
random.shuffle(l_otp)
final="".join(l_otp)




server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

username="pardhu4563@gmail.com"
password="ntlo uskz rwlq foij"

server.login(username,password)



receiver=input("enter reciver mail:")

##subject=input("subject:")
##text=input("matter:")

#mail=f"{subject}\n\n{text}"

server.sendmail(username,receiver,final)


print("mail sent successfully")

'''


#otp sending through mail:

import smtplib
import random
import string

otp=""
for i in range(3):
    otp+=str(random.randint(1,9))
for j in range(3):
    otp+=random.choice(string.ascii_letters)

l_otp=list(otp)
random.shuffle(l_otp)
final="".join(l_otp)

username="pardhu4563@gmail.com"
password="ntlo uskz rwlq foij"


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(username,password)

receiver=input()
server.sendmail(username,receiver,final)

print(f"mail sent succesfully to {receiver}")



















 





