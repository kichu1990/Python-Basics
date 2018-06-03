#How do you retrieve 5th character of a string "we are learning python" ?

str="we are learning python" 
str[5]

#Construct an integer from the string "12345"
x="12345"
type(x)
y=int(x)
type(y)

#use slice operator to retrieve alternate characters; use slice operator to retrieve every 3rd character 
#str2='this is a great learning on python'
str2.split()



#How do you retrieve 'l' char of a string "we are learning python" 



#List
#Construct a list of integers
list_int=[1,2,3,4,5]

#Construct a list of strings
list_string=["Physics", "Chemistry", "Maths", "English"]

#Construct a list of integers and strings
list_strint=["Physics", "Chemistry", "Maths", "English",1,2,3]

#Write a code print the length of a list
len(list_int)

#Write a code to print each item in the list
print(list_int)

#Write a code to append an item to a list
list_int.append(6)

#Write a code to insert an item at the beginning of a list. 
list_int.insert(0,9)

#Removing Given Object from List
list_int.remove(9)

#Write a code to insert an item in the middle of a list. 
list_int.insert(3,12)

#Write a code to add two lists together, using both the extend method and the plus
#(+) operator and note the difference 
list_int+list_string

#Write a code to retrieve the 4th item from list. 
list_int[4]

#Write a code to retrieve the 2nd, 3rd, and 4th items from the list. 
list_int[1:4]

# Write a code to replace an item in a list with a new item. 
list_int[3]=15


str3='python is a good scripting language'
str3[:]
str3[0:]
str3[:35]

#Write a function to append items to an empty list. 

#Implement a stack using list
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()

#Implement a queue using list
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")          
queue.append("Graham")         
queue.popleft()                
queue.popleft()     
