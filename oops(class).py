#oops:
#pop --> top to bottom approach
#oops ---> bottom to top  approach

#class   ---> blueprint
#object  ---> instace of the class
#attributes ---> varibles
#if we write inside the -->class attributes
#instance(__init__) ---> instance attributes


#methods  ---> functions (actions)

#define class:

'''
class Classname():
    a=10 #class attributes
    b=20

obj1=Classname() #object creation
print(obj1.a)
print(obj1.b)

obj2=Classname()
print(obj2.a)
print(obj2.b)
print(obj1.a)
'''


#class with vehicle:
'''
class Vehicle():
    color="red"
    brand="bmw"
    model=2025


car1=Vehicle()
print(car1.color)
print(car1.brand)
print(car1.model)

bk=Vehicle()
bk.color="white"
print(bk.color)

print(car1.color)
'''











#method:  function
'''
class Studentdetails():
    def __init__(name,age,marks):
        name=name
        age=age
        marks=marks

    def s_details():
        print(name,age,marks)


s1=Studentdetails("sidhu",24,655)
s1.s_details()

s2=Studentdetails("john",43,234)
s2.s_details()'''


'''
class Studentdetails:
    def __init__(self,n,a,m):
        self.name=n
        self.age=a
        self.marks=m

    def s_details(self):
        print(self.name,self.age,self.marks)


s1=Studentdetails("sidhu",24,655)
s1.s_details()

s2=Studentdetails("john",43,234)
s2.s_details()



'''



#constructor: __init__
'''
class Bike():
    def __init__(self,color,speed,model):
        self.c=color
        self.s=speed
        self.m=model
        

color=input()
speed=input()
model=input()

b1=Bike(color,speed,model)  #instance object
print(b1.c)
print(b1.s)
print(b1.m)'''


'''
class Bike():
    def __init__(self):
        self.c=color
        self.s=speed
        self.m=model
        

co=input()
sp=input()
mo=input()

b1=Bike()  #instance object
print(b1.c)
print(b1.s)
print(b1.m)
'''

#access specifiers:
#public
#private
#protected


'''
class BankAct():
    def __init__(this,name,balance,ids):
        this.n=name  #public
        this._b=balance  #protected
        this.__id=ids     #private

    def details(self):
        print(self.n,self._b,self.__id)



user1=BankAct("john",420,7234)
##print(user1.n)
##print(user1._b)
##print(user1._BankAct__id)   #mangling
user1.details()


'''


'''
class Details:
    place="vijaywada"    #class attribute    always clas attribute(common)
    
    def __init__(self):
        self.name=input("enter name")   #instance attribute (changes)
        
    def data(self):
        print(self.name,self.place)

d1=Details()
d1.data()

d2=Details()
d2.data()
'''






'''
class Bank:
    
    def __init__(self,name,balance,pin):
        self.name=name
        self.__balance=balance  #private(__)
        self.pin=pin
        

    def deposit(self,amount):
        checkpin=int(input("enter pin"))
        if self.pin==checkpin:
            if amount>0:
                if amount%100==0 or amount %500==0 or amount %2000==0:
                    self.__balance+=amount
                    print("succesful")
                else:
                    print("amount accept only 100 or 500 or 2000")
            else:
                print("invalid amount")
        else:
            print("invalid pin")

    def check_balance(self):
        print(self.__balance)
        

b1=Bank("paul",1000,1234)
b1.deposit(200)
b1.check_balance()
'''



#inheritance:
#single inheritance:
'''

class Grandparent:
    def grandparentmethod(self):
        print("this is grandparent method")

class Father(Grandparent):
    def fathermethod(self):
        print("this is father method")
        

f1=Father()
f1.fathermethod()
f1.grandparentmethod()

'''


#multi_level inhertiance:
'''
class Grandparent:
    def grandparentmethod(self):
        print("this is grandparent method")

class Father(Grandparent):
    def fathermethod(self):
        print("this is father method")

class child(Father):
    def childmethod(self):
        print("this is child method")

c1=child()
c1.childmethod()
c1.fathermethod()
c1.grandparentmethod()
'''



'''

#multiple inhertance:
class Father:
    def method(self):
        print("this is father method")

class Mother():
    def method(self):
        print("this is Mother method")

class child1(Mother,Father):
    def cmethod(self):
        print("this is child method")



c1=child1()
c1.method()
'''

##print(child1.__mro__)    #method resolution order
##print(Mother.__mro__)

'''
#hierarchical inheritance:
class Parent:
    def parentm(self):
        print("this is parent method")

class Child1(Parent):
    def child1m(self):
        print("this is child1 method")

class Child2(Parent):
    def child2m(self):
        print("this is child2 methods")

c2=Child2()
c2.child2m()
#c2.child1m()
c2.parentm()


print(Child2.__mro__)
'''


'''
class Details:
    def __init__(self,name,email,phone_no,address,qualification):
        self.name=name
        self.email=email
        self.phone_no=phone_no
        self.address=address
        self.qualification=qualification

    def change_name(self,new_name):
        print(f"succefulll changed {self.name}--> {new_name}")
        self.name=new_name

class Development(Details):
    def __init__(self,name,email,phone_no,address,qualification,experience,project):
        super().__init__(name,email,phone_no,address,qualification)
        self.experience=experience
        self.project=project

    def data(self):
        print(self.name,self.experience,self.project)


class Student(Details):
    def __init__(self,name,email,phone_no,address,qualification,batch_no,course):
        super().__init__(name,email,phone_no,address,qualification)
        self.batch_no=batch_no
        self.course=course

    def data(self):
        print(self.name,self.batch_no,self.course)

'''

    

##d1=Development("bal","bal@gmail.com",5678,"address","CSE",2,"LMS")
##d1.data()
##d1.change_name("john")

s1=Student("devi","devi@gmail.com",2134,"fever","mtech",118,"pfs")
s1.data()
s1.change_name("sharon-rose")
print(Student.__mro__)
        
        
    

#method overloading:
'''
class Calculation:
    def add(self,a=0,b=0,c=0):
        return a+b+c

cl=Calculation()
print(cl.add(10,20))
print(cl.add(10,20,30,40))
print(cl.add(5))
'''


'''
class Calculation:
    def add(self,*a):
        print(sum(a))

c1=Calculation()
c1.add(10,20,3,67)
'''

'''
class Calculation:
    def add(self,*a):
        s=0
        for i in a:
            s+=i
        print(s)
            

c1=Calculation()
c1.add(10,20,3,67,567)
'''


#Abstraction:
#hiding the unneccessary data:
'''
from abc import ABC,abstractmethod
class Base(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass

class Bottom(Base):
    def m1(self):
        print("this is m1 class")
    def m2(self):
        print("this is m2")


##b1=Base()
##b1.m1()

bo1=Bottom()
bo1.m2()
'''
    




'''
from abc import ABC ,abstractmethod
class Cls(ABC):
    @abstractmethod
    def payment(self):
        pass
    @abstractmethod
    def m2(self):
        print("this is cls m2")

class Cls2(Cls):
    def m1(self):
        print("this is cls2")

    def m2(self):
        print("this is m2 cls")

c=Cls2()
c.m2()
'''














'''
from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def paying(self):
        print("cash")

class credit_card(payment):
    def paying(self):
        print("paying using paytm")

class debit_card(payment):
    def pay(self):
        print("paying with debit card")

##c1=debit_card()
##c1.paying()

c2=credit_card()
c2.paying()
'''






#contact management system:
#phonebook
#adds--> number,name
#update --> name or number update
#delet ---> delet contact details












