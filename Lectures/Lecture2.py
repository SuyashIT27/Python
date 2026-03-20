#String store sequence of character 
#escape sequence character is used to format our string 
# String concatnitation 
str1="hello"
str2=" word"
print(str1+str2)
#len() is used to get the length of the string 
print(len(str1))
# to get the character at the index 
print(str1[3])
#string are immutabele
#slicing means accesing parts of the string 
print(str1[0:2])
#we can do backword counting in python using the negative index start from -1
print(str1[-1])
str = "I am a coder."
str.endswith("er.") #returns true if string ends with substr
str.capitalize() #capitalizes 1st char
str.replace( "I", "Hii") #replaces all occurrences of old with new
str.find("Hii") #returns 1st index of 1st occurrence
str.count("am") #counts the occurrence of substr in string

#WAP to input user's first name & print its length.
name=input("Enter the name")
print(len(name))

#Conditional Statement 
age=int(input("Ener your age"))
if(age>=18):
  print("Yes,he is elegible")
else:
  print("No you are not elegible") 
#elif it is used to check multiple condition 
