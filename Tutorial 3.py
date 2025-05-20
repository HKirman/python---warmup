#Arithmatic Operations
print(2 + 5)      #Addition
print(2 - 5)      #Substraction
print(2 * 5)      #Multiplication
print(50 / 5)     #Division
print(2 ** 5)     #Exponential
print(10 % 3)     #Returns the remainder when the first number is divided by the second number.
print(10 // 4)    #Rounds the result of dividing two numbers to the smallest number.
print(-10 // 4)

#Assigment Operators
x=10
x=x+10      #Adds 10 to x to create a new x value. Both representations are correct.
x+=10
print(x)

y=5         #Multiply y by 2 to create a new y value
y*=2
print(y)

z=8         #Divided z by 2 and created a new z value
z/=2
print(z)

#Comparison Operators

#The result of the comparison operator always returns a boolean value, that is, true or false.
'''
==  equal
!=  Not equal
<   less than
>   greater than
<=  less than or equal to
>=  greater than or equal to

'''

print(10<20 and 2>10)       #True when both cases are true and false when the other cases are false
print(1>50 or 5<6)          #Only true if one of them is true
print(not False)            #Inverse of boolean value
print(not 10<20)

print()

m=10
n=20
print(m==n)
print(m<n)
print(m<=n)
print(m!=n)

print()

k="Hello"
l="Hi"
print(k==l)

print()

t= input("Enter first number: ")        #Gets the user to enter a number
p= input("Enter second number: ")

t=int(t)                                #Assigns the received value to the t value
p=int(p)

print(t)                                #print t value
print(p)
print(t+p)                              #sum and print