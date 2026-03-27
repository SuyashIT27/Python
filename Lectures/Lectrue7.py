# FILE I/O IN PYTHON
# TO open the file 
#file=open("Filename","mode")
f=open("demo.txt","r")
data=f.read()
print(data,type(data))
f.close()
#.readline() is used to read one line at a time 
# Writing the data in the file 
w=open("demo.txt","w")
w.write("I am from ABES ENGINEERING COLLEGE")
w.close()
# if file is not avaliable then it will get created 
#r+ is used to write in the file at rhe starting by overwriting
# a+ is used to append the text at the ending 

#mordern way is to use with
with open("demo.txt","r") as c:
  print(c.read(),"2")
# it is not compulsery to use close() when using the with 

# deleting a file 
# to delete a file os module is used we need to import it 
import os
os.remove("demo.txt")\

# question practice 
practice=open("practice.txt","w")
practice.write("Hii everyone\n")
practice.write("we are learning File I/O\n")
practice.write("using the Java\n")
practice.write("i like programming in java\n")
practice.close()
with open("practice.txt","r") as seeing:
  print(seeing.read())

 



