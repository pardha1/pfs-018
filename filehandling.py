#File handling:  -->READ,WRITE,UPDATE,DELET

#r --->read
#w --->write
#a --->append
#r+ ---> read+write
#w+ --->write +read

#file reading:

'''

f=open('C:/Users/pardh/OneDrive/Desktop/python_018/testing.txt','r')
#print(f.read())
print(f.read(3))
#print(f.readlines())
#print(f.readline(),end="")
#print(f.readline())

print(f.readlines())

'''



#file write: with append
'''
f=open('C:/Users/pardh/OneDrive/Desktop/python_018/testing.txt','a')

f.write("This is data i am inserting")

f.close()
'''



#read + , file must :
'''
f=open("C:/Users/pardh/OneDrive/Desktop/python_018/testing.txt","r+")
print(f.read())
f.write("python data ")
f.close()
'''

#write+ , createa new file:
'''
f=open("C:/Users/pardh/OneDrive/Desktop/python_018/testing.txt","w+")
print(f.read())
f.write("python data ")
f.close()
'''




#img:
f=open('code.jpeg',"rb")
print(f.read())
f1=open('coder.jpeg',"wb")
for i in f:
    f1.write(i)
f.close()


##with open("file","r,w,rb") as f:
##    print(f.read())
    


















































