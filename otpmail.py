import random
import string
import smtplib
try:
    username="akhilathotakura3@gmail.com"
    password="xqculhhwnlurtdor"

    otp=""
    for i in range(3):
        otp+=str(random.randint(0,9))

    for j in range(3):
        otp+=random.choice(string.ascii_letters)

    l_otp=list(otp)
    random.shuffle(l_otp)
    final="".join(l_otp)

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()   #transfer layer security
    receiver=input("enter email:")


    server.login(username,password)


    server.sendmail(username,receiver,final)

    print("otp sent succefully")
except Exception as e:
    print(e)




