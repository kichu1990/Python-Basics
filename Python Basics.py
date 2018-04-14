
# coding: utf-8

# In[3]:


#Datatype in Python


# In[6]:


1+1


# In[7]:


2*9


# In[9]:


4/2


# In[10]:


5%2


# In[11]:


8-5


# In[12]:


#Variable Assignement


# In[13]:


var=2


# In[15]:


var


# In[17]:


'Single Quote'


# In[18]:


"double quote"


# In[20]:


x="double quote"


# In[21]:


x


# In[22]:


print(x)


# In[23]:


num=12


# In[24]:


name="Sam"


# In[26]:


print("My name is {} and age is {}".format(name,num))


# In[27]:


print("My name is {one} and age is {two}".format(one=name,two=num))


# In[28]:


s="hello"


# In[29]:


s[0]


# In[31]:


print(s[0])


# In[32]:


print(s[:2])


# In[33]:


s[2:]


# In[34]:


#List in Python


# In[35]:


my_list=["a","b","c"]


# In[36]:


my_list[1]


# In[38]:


nest=[1,2,[3,4]]


# In[39]:


nest[2]


# In[40]:


nest[2][1]


# In[41]:


nest=[1,2,[3,4,["New"]]]


# In[43]:


nest[2]


# In[44]:


nest[2][2]


# In[45]:


nest[2][2][0]


# In[46]:


#Dictionary in Python


# In[47]:


my_Dict={'k1':'abc','k2':12,'k3':'efg'}


# In[48]:


my_Dict


# In[49]:


my_Dict['k1']


# In[50]:


my_Dict_1={'k1':[1,2,3]}


# In[51]:


my_Dict_1['k1']


# In[52]:


my_Dict_1['k1'][1]


# In[53]:


my_Dict_1['k1'][1]=5


# In[54]:


my_Dict_1['k1'][1]


# In[55]:


my_Dict_1['k1']


# In[56]:


#Tuples in python


# In[57]:


my_Tuple=(1,2,3,4,5)


# In[58]:


my_Tuple[1]


# In[60]:


my_Tuple[1]=9


# In[61]:


#set function


# In[62]:


my_List=[1,1,1,1,2,2,2,2,2,4,4,4,4]


# In[63]:


set(my_List)


# In[64]:


#Logical operator 


# In[65]:


1==1


# In[66]:


1!=2


# In[67]:


1>2


# In[68]:


(1>2) and (2<1)


# In[70]:


(1<2) or (2>1)


# In[71]:


#ifelse in Python


# In[73]:


if 1<5:
    print("Yep!")
else:
    print("damn")


# In[74]:


if 1<3:
    print("First")
elif 1==1:
    print("Equal")
else:
    print("Damn")
    

