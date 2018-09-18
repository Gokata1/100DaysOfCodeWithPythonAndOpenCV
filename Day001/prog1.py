# both double quotes and single quotes work similarly(atleast in case of print statement)
print ('Hello, World!!')

#NOTE: ':' semicolan is important in such statments like for, while if etc
#Indention is very important other wise you will get error
if(5>2):
    print ("This is true..")

#This does not work as the indention after if statement is not proper
# if(4<7):
# print ("This is also true")

# As can be seen # is used to initiate an inline comment
"""This is a docString. A docstring is used when in module, function, class, or method definition.
They are used to create documentation of a component. It can be multi-line as seen here.
Docstring in the middle of a file can also be used for documentation"""

#Following are some examples of variables.
#As can be seen there is no type defination in python the variable is assigned the type when it
#is give a value
x = 5
y = 'John'
print (x)
print (y)

#A variable does not have a set type and can be changed even after assignment
x = 'Sammy'
print (x)

#Variable names in python are case sensitive 
age = 5
agE = 6
Age = 7
print (age)
print (agE)
print (Age)

#This does not work because we can not merge string and number
#print ("Age is" + Age)

#This works as both are strings
x = 'Awesome'
print ("Python is " + x)