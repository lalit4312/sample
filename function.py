# def login():
#     print("python")
# login()    

# def login():
#     print("hello world")
# def login2():
#     print("python\n"*5,end="")    
# login()
# login2()

# def add():
#     x=10
#     y=20
#     c=x+y
#     print(c)
# add()    

# def login(username,password):
#     print(f"your username is:{username} and your password is:{password}")
# login("sunil","battle")    

# def function(num1,num2):
#     print(num1*num2)
# function(4,2)    
    
# def pw(x,y):
#     z=x**y        #positional argument
#     print(z)
# pw(5,2)    

# def show(name,age):
#     print(f"name:{name} age:{age}")   #keyword argument
# show(name="sunil",age=20)

# def show(name,age=20):
#     print(name,age)     #defult argument
# show(name="sunil")    

# def show(name,age=20):
#     print(name,age)       #garbage collection
# show(name="sunil",age=30)    

# def show(*num):
#     z=num[0]+num[1]+num[2]  #varaible length argument
#     print(z)
# show(5,4,3)    

# def show(**num):
#     z=num['a']+num['b']+num['c']  #keyword length variable argument
#     print(z)
# show(a=5,b=4,c=3)

#Add Two Number using function
# def add(x,y):
#     return x+y
# x=int(input("enter a number"))
# y=int(input("enter another number"))
# z=x+y
# print(z)

# def add():
#     x=10
#     y=20
#     z=x+y
#     return x+y
# print(add())  
 
#Find 2 Max value using function in python
# def max(c,v):
#     if c>v:
#         return c
#     else:
#         return v
# b=max(3,4)
# print("the greatest number is:",b)            
    
#Find 3 Max Value using function in python    
# def max(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b 
#     else:
#         return c
# d=max(8,7,9)
# print("the maximum is:",d)

#Find last character in name using function in python
# def character(a):
#     return a[-1]
# a="lalit"
# r=character(a)
# print("last character is:",r)


# def character(a):
#     return a[-1]
# a=input("enter the name")
# r=character(a)
# print("last character is:",r)

#Write a Python function to multiply all the numbers in a list. Sample list = [8,2, 3, -1,7]
# def multiple(a):
#     b=1
#     for i in a:
#         b*=i
#     return b
# print(multiple((8,2,3,-1,7)))

                   #task
#1.  Write a Python function to multiply all the numbers in a list.Sample list = [8,2,3,-1,7]
# def sample(a):
#     a=[8,2,3,-1,7]
#     b=1
#     for i in a:
#         b*=i
#     return b
# print(sample((8,2,3,-1,7))) 

#2.  Write a Python function to sum all the numbers in a list.Sample list : [8, 2, 3, 0, 7]
# def sample(a):
#     a=[8,2,3,0,7]
#     b=0
#     for i in a:
#         b+=i
#     return b 
# print(sample((8,2,3,0,7)))       

#3.  Write a python function to find min of three numbers.(no parameter and no return type)
# def min():
#     a=2
#     b=3
#     c=4
#     d=(a+b+c)/3
#     print(d)
# min()

# 5. Create a function that can accept two arguments name and age and print its value
# def function(name,age):
#     print(f"your name is {name} and your age is {age}")
# name=input("enter your name:")  
# age=int(input("enter your age"))
# function(name,age)  

    
# def add(a,b):
#     return a+b  #single value
# c=(add(2,3))
# print(c)


#multiple value
# def add(a,b):
#     c=a+b
#     d=a-b
#     return c,d
# print(add(10,5))

# def add(a,b):
#     c=a+b
#     d=a-b
#     e=a/b
#     f=a*b
#     return c,d,e,f
# print(add(10,20))    

# def max(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b 
#     else:
#         return c
# d=max(5,3,8)
# print("max number is:",d)        

# def add():  # no argument no return value
#     a=10
#     b=20
#     mult=a*b
# print(add())    

# def add():
#     a=10      #no argument with return value
#     b=20
#     c=a+b
#     return c
# print(add())    

# def add(a,b):
#     c=a+b
#     return c
# print(add(10,20))    

# def greeter(name):
#     print("good morning")
#     print("hello" + name)
# print("go")
# greeter("world")    

# def disp():
#     def show():
#         print("show function")
#     print("disp function")
#     show()    
# disp()

# def disp():
#     def show():
#         return "show function"
#     result=show() + " disp function"
#     return result
# a=disp()
# print(a)

# def inner():
#     x=4
#     print(x)
# inner()    

# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         print(x)
#         print("inside the function y", y)
#     inner()
#     print("z:", z)
# outer()        

# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         nonlocal z #nonlocal can change value inside nested function
#         z=z+1
#         global y#global change value of global area
#         y=y+2
#         print(x)
#         print("inside the function y", y)
#     inner()
#     print("z:", z)
# outer()        

# y=10
# def inner():
#     x=4
#     print(x)
#     print("inner the function y", y)
# print("y:", y)
# inner()    

# y=10
# def inner():
#     x=4
#     global y
#     y=y+1
#     print(x)
#     print("inner the function y", y)
# print("y:", y)
# inner()

# x=10
# def outer():
#     x=4
#     def inner():
#         x=8
#         print(x)
#     inner()
# outer()        


# def outer():
#     x="local"
#     def inner():
#         nonlocal x
#         x="nonlocal"
#         print("inner: ", x)
#     inner()
#     print("outer:", x)
# outer()        


#anonymous function(lambda function)
# result=lambda n1,n2,n3:n1+n2+n3
# print("sum of three value : ", result(10,20,25))

# result=lambda n1,n2,n3:n1*n2*n3
# print("multiplication:", result(2,3,4))

# add_sub=lambda x,y:(x+y, x-y)
# a,b=add_sub(5,2)
# print(a)
# print(b)

#map function
# li=[5,7,22,97,54,62,77,23,73,61]
# square_list= list(map(lambda x: x**2, li))
# print(square_list)

# a=[1,2,3]
# b=[3,4,5]
# abc=list(map(lambda x,y:x+y,a,b))
# print(abc)

#filter()function
# data=[1,2,3,4,5,5,6,6,7,9,10]
# var=list(filter(lambda x: x%2==0, data))  # jun true hunxa tei output hunxa
# print(var)

#reduce()function
# from functools import reduce 
# li=[5,8,10,20,50,100]
# sum=reduce((lambda x,y: x+y), li)
# print(sum)







