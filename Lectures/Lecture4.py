#Dictionary are used to store the data in key:value form
#it can store multiple datatype
myInfo={
  "name":"Suyash Verma",
  "age":21,
  "College":"ABES ENGINEERING COLLEGE"
}
print(myInfo)
#To access the particular key 
print(myInfo["College"])
#Dictionary are mutable 
myInfo["College"]="IIT DELHI"
myInfo["Year"]=3
print(myInfo)
#we can make the null disctionary 
null_dict={}
# we can make the nested disctionary 
student2={
  "name":"Suyash Verma",
  "Subject":{
    "phy":85,
    "math":90,
    "chemistry":95
  },
  "roll_no":257,
}
print(student2["Subject"]["phy"])
#Mehod in Dictinoery 
print(student2.keys())
print(len(student2))
print(list(student2.values()))
print(student2.items())#return all the key value pair 
student2.update({"location":"Ghaziabad"})

#SETS IN PYTHON 
#Set is the collection of the unordered items.
#Each element in the set must be unique & immutable.
sets={1,2,3,4,1,4}
print(sets)
# to make the empty set 
emptySet=set()
#elements of the set are immuatble 
sets.add(45)
sets.remove(2)
print(sets)
#sets can store multiple datatype 
sets.clear()
print(sets)
set1={2,4,6,7,3}
set2={34,65,78,95}
set3=set1.union(set2)
print(set3 )
