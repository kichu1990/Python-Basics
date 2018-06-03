
# coding: utf-8

# In[2]:


#1. How do you retrieve 5th character of a string "we are learning python" ?


# In[5]:


str="we are learning python" 


# In[6]:


str[5]


# In[120]:


#Construct an integer from the string "12345"
x="12345"
type(x)
y=int(x)
type(y)


# In[132]:


#use slice operator to retrieve alternate characters; use slice operator to retrieve every 3rd character 
#str2='this is a great learning on python'
str2.split()


# In[8]:


#How do you retrieve 'l' char of a string "we are learning python" 


# In[119]:


#List


# In[10]:


#Construct a list of integers


# In[79]:


list_int=[1,2,3,4,5]


# In[12]:


#Construct a list of strings


# In[13]:


list_string=["Physics", "Chemistry", "Maths", "English"]


# In[14]:


#Construct a list of integers and strings


# In[18]:


list_strint=["Physics", "Chemistry", "Maths", "English",1,2,3]


# In[19]:


#Write a code print the length of a list


# In[28]:


len(list_int)


# In[22]:


#Write a code to print each item in the list


# In[89]:


print(list_int)


# In[25]:


#Write a code to append an item to a list


# In[81]:


list_int.append(6)


# In[40]:


#Write a code to insert an item at the beginning of a list. 


# In[83]:


list_int.insert(0,9)


# In[44]:


#Removing Given Object from List


# In[47]:


list_int.remove(9)


# In[51]:


#Write a code to insert an item in the middle of a list. 


# In[85]:


list_int.insert(3,12)


# In[57]:


#Write a code to add two lists together, using both the extend method and the plus
#(+) operator and note the difference 


# In[87]:


list_int+list_string


# In[62]:


#Write a code to retrieve the 4th item from list. 


# In[63]:


list_int[4]


# In[64]:


#Write a code to retrieve the 2nd, 3rd, and 4th items from the list. 


# In[68]:


list_int[1:4]


# In[70]:


# Write a code to replace an item in a list with a new item. 


# In[88]:


list_int[3]=15


# In[ ]:


str3='python is a good scripting language'
str3[:]
str3[0:]
str3[:35]


# In[76]:


#Write a function to append items to an empty list. 


# In[90]:


#Implement a stack using list


# In[95]:


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()


# In[99]:


#Implement a queue using list


# In[109]:


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")          
queue.append("Graham")         
queue.popleft()                
queue.popleft()     

