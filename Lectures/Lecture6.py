# Function is the block of code that perform certain task
def sum(a,b):
  return a+b
c=sum(4,6)
print(c)
# if a function is called withour any implementation then it will return NONE
#Funtion is of two type buildin and user defined 
# to print two print statement wihout new line use end=" ";
print("Hello" ,end=" ")
print("world")
#Default Parameters
#Assigning a default value to parameter, which is used when no argument is passed.

#When a function called itself then it is known as the recursion 

#Print number from 1 to n
def numSeries(n):
  if(n==1):
    print(1)
    return
  numSeries(n-1)
  print(n)
numSeries(6) 
# Print he factorial of the number 
def factorial(n):
  if(n==1):
    return 1
  return factorial(n-1)*n 
print(factorial(5))  