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

#Given a list of strings, return the count of the number of strings where the string length
#is 2 or more and the first and last chars of the string are the same.
def match_words (words):
    count=0
    for word in words:
        if len(word)>0 and word[0]==word[-1]:
             count+=1
    return count

#Given a list of strings, return a list with the strings in sorted order, except group all
#the strings that begin with 'x' first
def front_x(words):
    list1.clear()
    list2.clear()
    count=0
    for word in words:
        if word[0]=='x':
            list1.append(word)
        else:
            list2.append(word)
        count+=1
    return count
list1.sort()
list2.sort()
print(list1+list2)

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

#Slicing of Strings
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
