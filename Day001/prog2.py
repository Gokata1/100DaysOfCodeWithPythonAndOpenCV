'''Python Support three numeric types int (5), float (7.5) and complex (5j,5+3j)'''
x = 6
y = 5.7
z = 1j

#type(variable) is used to show the class of the variable 
print(type(x))
print(type(y))
print(type(z))

#int can be of unlimited length with no decimals

#float can also be a scientific number
a = 35e3
b = 12E4
c = -87.7e100

print (a)
print (type(a))
print (b)
print(type(b))
print (c)
print (type(c))

#Complex numbers are written with j as imaginary part
x = 3+5j
print (x)
print (type(x))

#Type casting is also used in python using constructors for int(), float() and str()
#Only suitable litrals can be type casted
# As this will not work
#y = float("trying")

#Other examples of type casting are as follows
i = int(5.7) #here the number is rounded of to the lower integer value
j = int("9") 
print (i)
print (j)

# This will not work as the string is converted to float
#k = int("6.7") 
#Type casting can be nested as shown below
k = int(float("6.7"))
print (k)

#Python does not have any character type. A character in python is just a string with single character
c = 'k'
print (c)

str = "Hello World"
print (str)
print (str[0])

#We can also print substrings of a string
print (str[2:6])
#This will print the element from 5th index till the end of the string
print (str[5:])

#it is also possible to use negative index for string
# H e l l o _ W o r l d
# 0 1 2 3 4 5 6 7 8 9 10
#-11-10-9-8-7-6-5-4-3-2-1
print (str[-7])
print (str[-4:]) #This print the string from negative index till end of the string

str = "  Hello !!!   "
print (str)
print (str.strip()) #This stips all the leading and trailing spaces from the string
# Following string methods are pretty self explanatory
print (len(str))
print (str.lower())
print (str.upper())
print (str.replace("H", "Y")) #Replace the first character with second character
print (str.replace('l','y')) #Replace every occurance of the character
print (str.replace('ll','l')) #In case of substring replace the complete substring

#In case of multiple occurance of the the same substring replace all the substrings with given substring
str = "aabaacaad"
print (str.replace('aa','1')) 

str = "Hello, World"
print (str.split(','))

#It does not work as the result of str.split() is an array and strip() is a string function
#print (str.split(",").strip())
