#Phonebook:

class PhoneBook():
    def __init__(self):
        self.contact={}


    def view(self):
        if not self.contact:
            print("empty")
        else:
            print(self.contact)

    def add(self,name,number):
        if name in self.contact.keys():
            print(f"{name} already exists")
        elif number in self.contact.values():
            print(f"{number} already exists")
        else:
            self.contact[name]=number

    def delet(self,name):
        if name in self.contact:
            del self.contact[name]
            print(f"{name} deleted succefully")
        else:
            print("name not in phonebook")


    def update(self,name,new_name=None,new_number=None):
        if name in self.contact:
            self.contact[new_name]=self.contact.pop(name)
            print("succefully named changed")
##        elif new_number:
##            self.contact[name]=new_number

        else:
            print(f"{name} not exists")
            
        
        
        
c1=PhoneBook()
c1.view()
c1.add("john",5678908098)
c1.add("says",456787654)
c1.view()
c1.update("john","joj")
c1.view()
c1.update("john","zam",123456789)
c1.view()
c1.update("joj","shyam",1899093909t)
c1.view()
