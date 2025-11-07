#regular expressions:

#match()
#search()
#findall()
#sub()
#split()

#regular expressions:
import re
#match()
'''
a="chintu bhai born on 2020"
b=re.match("chn",a)
c=re.match("sai",a)
d=re.match("bhai",a)

print(b)
print(c)
print(d)
'''

#search()
'''
x="found python found in 1992 found"
y=re.search("found",x)
print(y)
'''

#findall():
#we get data in list
'''
x="bharath ane nenu codegnan loo 1 month loo job kodtuna "
y=re.findall("loo",x)
print(y)
'''


#sub
'''
a="bharath ane nenu python demo avg ga echa"
y=re.sub("bharath ane nenu python demo avg ga echa","bharath ane nenu python demo baga ga echa",a)

print(y)
'''

'''
#split():
a="entra babu ee gola ee python"
b=re.split("ee",a)
print(b)

'''










#form validation --using regualar expressions:
#name --->letters,small or capital
#email  -->small letters,numbers,symbols,@,letters,.,letters
#phone_no
#password
#conform password


import re

def name_patter(name):
    return re.match("^[\D]{3,8}$",name)

def phone_no(phone):
    return re.match("^[6,9][\d]{9}$",phone)

def email_patter(email):
    #return re.match("^[a-z0-9]{1,9}@[a-z]{1,4}\.[a-z]{1,3}$",email)
    return re.match("^[a-z\d]{1,9}@[a-z]{1,4}\.[a-z]{1,3}$",email)

def password_patter(passoword):
    return re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[@$#*_]).{5,8}$",password)






name=input("Enter name:")
phone=input("Enter number:")
email=input("Enter a email")
password=input("enter password")
if not name_patter(name):
    print("invalid name")
elif not phone_no(phone):
    print("invalid phone")
elif not email_patter(email):
    print("invalid email")
elif not password_patter(password):
    print("invalid password")
else:
    print("success")





































