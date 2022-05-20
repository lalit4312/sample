# a=30
# b=20
# if a>b:
#     print("a is greater")
# else:
#     print("a is smaller")


# a=int(input("enter any number"))
# if a==1:
#     print("i like pant")
# elif a==2:
#     print("i like jacket")
# elif a==3:
#     print("i like shoes")
# elif a==4:
#     print("i like shirt")
# else:
#     print("i don't like anything")

#1.
# a=int(input("enter any number"))
# b=int(input("enter another number"))
# if a==b:
#     print("1")
# elif a>b:
#     print("2")
# else:
#     print("3")

#2.
# a=int(input("enter any number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# d=int(input("enter a number"))
# if (a==b) and (c==d):
#     print("hello")
    
#3.
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# d=int(input("enter a number"))
# if (a==b) or (c==d):
#     print("Hello")

#4.
# x=int(input("enter a number"))
# if x > 0:
#     print("positive")
# elif x < 0:
#     print("negative")
# else:
#     print("zero")

#5.
# a=int(input("enter a number"))
# if a % 2==0:
#     print("even")
# else:
#     print("odd")


#6.
# a=int(input("enter marks in 1 subject"))
# b=int(input("enter the marks in 2 subject"))
# c=int(input("enter the marks in 3 subject"))
# d=int(input("enter the marks in 4 subject"))
# total=a+b+c+d
# print(f"the total marks is{total}")
# percentage=((total/400)*100)
# if percentage > 70 :
#     print("distication")
# elif percentage > 60 :
#     print("first")
# elif percentage > 40 :
#     print("pass")
# else:
#     print("fail")


#7
# a="APPLE"
# a= a.lower()
# print(a)

#8.
# a=input("enter your name")
# b=input("enter your age")
# c=input("enter your address")
# print(f"your name is{a}")
# print(f"your age is{b}")
# print(f"your address is{c}")


#9.
# from cmath import pi
# radius=int(input("enter the radius of circle"))
# area=(pi)*((radius**2))
# print(f"area of circle is{area}")


#1. What is the output of ‘banana’ > ‘BANANA’?
# a="banana"
# a=a.upper()
# print(a)

#2. Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]
# natural=[1,2,3,4,5]
# for i in natural:
#     i=i+1
# if i==1:
#     print("5 is in the list of first five natural nunber")
# else:
#     print("5 is not in first five natural number")

#3. Given three integers, print the smallest one. (Three integers should be user input)
# a=int(input("enter a intiger"))
# b=int(input("enter a intiger"))
# c=int(input("enter a intiger"))
# if (a<b) and (a<c):
#     print(f"{a} is smallest among all three numbers")
# elif (b<c) and (b<a):
#     print(f"{b} is smallest among three number")
# else:
#     print(f"{c} is smallest anong three numbers")


#4. Given a three-digit number. Find the sum of its digits
# a=int(input("enter a three digit number"))
# b=int(input("enter a three digit number"))
# c=int(input("enter a three digit number"))
# d=a+b+c
# print(d)

# 5. Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, where 
# 1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. The program should display an error message if the user enters a number
# that is outside the range of 1 to 12.

# a=int(input("enter a day"))
# if a==1:
#     print("january")
# elif a==2:
#     print("febrary")
# elif a==3:
#     print("march")
# elif a==4:
#     print("april")
# elif a==5:
#     print("may")
# elif a==6:
#     print("june")
# elif a==7:
#     print("july")
# elif a==8:
#     print("august")
# elif a==9:
#     print("september")
# elif a==10:
#     print("october")
# elif a==11:
#     print("noveber")
# elif a==12:
#     print("december")
# else:
#     print("none")    


#  for i in range(5):
#      print("python")

#  for i in range(100):
#      print("python")


# name="A"
# Name="B"
# naMe="C"
# NAME="D"
# n_a_m_e="E"
# _name="F"
# name_="G"
# _name_="H"
# na56me="I"
# print(name,Name,naMe,NAME,n_a_m_e,_name,_name_,na56me)

#addition
# a=20
# b=30
# c=a+b
# print(c)

#subtraction
# a=20
# b=30
# c=a-b
# print(c)

#division
# a=20
# b=30
# c=a/b
# print(c)

#multiplication
# a=20
# b=30
# c=a*b
# print(c)

#reminder
# a=20
# b=30
# c=a%b
# print(c)

#exponent
# a=20
# b=30
# c=a**b
# print(c)

#floor division
# a=20
# b=30
# c=a//b
# print(c)

# a=21
# b=10
# if (a==b):
#     print("a is equal to b")
# else:
#     print("a is not equal to b")

# if (a!=b):
#     print("a is not equal to b")
# else:
#     print("a is equal to b") 

# if (a<b):
#     print("a is less than b")
# else:
#     print("a is not less than b")

# if (a>b):
#     print("a is greater than b")
# else:
#     print("a is not greater than b")


# a=5;
# b=20;
# if (a<=b):
#     print("a is either less than or equal to b")
# else:
#     print("a is neither less than or equal to b")

# if (b>=a):
#     print("b is either greater than b oe equal to b")
# else:
#     print("b is neither greater than nor equal to b")           


# for i in range(10):
#     if (i==5):
#         continue
#     print(i)
# print("rest of the code")


# WAP to enter amount and calculate discounts on the following basis?if the amount is greater than 10000 then discount will ber 10%
# otherwise the discount will be 5%.calculate the total amount?
# a=int(input("enter the amount"))
# if a>=10000:
#     d=(a*10)/100
# else:
#     d=(a*5)/100
# print("discount:",d)
# print("net pay:",(a-d))

# a=50
# b=20
# c=90
# print(a>b or c)
              
# a=20
# b=30
# c=60
# print(a>b or c)

# a=10
# b=10
# print(a is b)

# x=5
# y='python'     #output:true
# print(x is not y)

#membership operator
# y="python"          #in
# print("th" in y)

#not in
# y="python"
# print("to" not in y)

#bitwise
# a=60
# b=13
# c=0
# c=a&b;
# print("value of c is",c)




for i in range(-3):
    print(i)






