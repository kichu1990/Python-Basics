#Operator in Python
1+1
2*9
4/2
5%2
8-5

#Variable Assignement
var=2
var
'Single Quote'
"double quote"
x="double quote"
x
print(x)
num=12
name="Sam"

print("My name is {} and age is {}".format(name,num))
print("My name is {one} and age is {two}".format(one=name,two=num))

s="hello"
s[0]
print(s[0])
print(s[:2])
s[2:]

#List in Python
my_list=["a","b","c"]
my_list[1]
nest=[1,2,[3,4]]
nest[2]
nest[2][1]
nest=[1,2,[3,4,["New"]]]
nest[2]
nest[2][2]
nest[2][2][0]

#Dictionary in Python
my_Dict={'k1':'abc','k2':12,'k3':'efg'}
my_Dict
my_Dict['k1']

my_Dict_1={'k1':[1,2,3]}
my_Dict_1['k1']
my_Dict_1['k1'][1]
my_Dict_1['k1'][1]=5
my_Dict_1['k1'][1]
my_Dict_1['k1']

#Tuples in python
my_Tuple=(1,2,3,4,5)
my_Tuple[1]
my_Tuple[1]=9

#set function
my_List=[1,1,1,1,2,2,2,2,2,4,4,4,4]
set(my_List)

#Logical operator 
1==1
1!=2
1>2
(1>2) and (2<1)
(1<2) or (2>1)

#ifelse in Python
if 1<5:
    print("Yep!")
else:
    print("damn")

if 1<3:
    print("First")
elif 1==1:
    print("Equal")
else:
    print("Damn")
    
#for Loop
sequence=[1,2,3,4,5]
for num in sequence:
    print num
    


