#List in pyhton
#a built-in data type that store set of values
#[] is tused to make list it is dynamic
marks=[90,67,54,98,70]
#To get the marks at the particular index 
print(marks[3])
#it can store mumtiple datatype they are mutable
#slicing in python 
print(marks[2:3])
marks.append(54)
marks.sort()
#marks.sort(reverse=True)
marks.insert(2,45)
print(marks)
#Tuple in data type that lets us create immutable sequence of values
#it is denotes by()
data=(2,4,6,3,7,9)
#it is same as list
print(data[2:4])
#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
num=int(input("Enter the range of the movie"))
movie=[]
for i in range(num):
  inputMovie=input("Enter the name of the movie")
  movie.append(inputMovie)
print("Movie name are")
print(movie)  







