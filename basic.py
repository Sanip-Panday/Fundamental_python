#Python program to add two numbers

# num1 = int(input("Enter first number:"));
# num2 = int(input("Enter  second number:"));

# sum = num1 + num2
# print("sum of num1 and num2 is:", sum)

# Define a lambda function to add two numbers
# add_numbers = lambda x, y: x + y

# # Take input from the user
# num1 = 1
# num2 = 2

# # Call the lambda function to add the two numbers
# result = add_numbers(num1, num2)

# # Print the result
# print("The sum of", num1, "and", num2, "is", result)




# #Maximum of two numbers in Python
# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))

# if (num1 > num2):
#     print("maximum number is :", num1);
# else:
#     print("maximum number is :", num2);






# Python Program for factorial of a number

# n = int(input("enter number"))
# result = 1
# for i in range(n,0,-1):
#     result = result * i
# print("factorial of ", n, "is:", result)

# Python Program for simple interest
# p = float(input("enter principle:"))
# t = float(input("enter time"))
# r = float(input("enter rate:"))

# def simple_interest(p,t,r):
#     si = (p*t*r)/100
#     print("simple interest is:", si)
#     return si

# simple_interest(p,t,r)


# QN.Python Program for compound interest
# A = P(1 + R/100) t 

# Compound Interest = A – P 

# def compound_interest(p,t,r):
#     amount = p*(pow((1 + r/100), t))
#     CI = amount - p
#     print("compound interest is :", CI)

# compound_interest(100,2,3)







 # QN.Python Program to check Armstrong Number
#  A positive integer is called an Armstrong number if an Armstrong number of 3 digits,
#  the sum of cubes of each digit is equal to the number itself


# n = 153 # or n=int(input()) -> taking input from user
# s = n # assigning input value to the s variable
# b = len(str(n))
# sum1 = 0
# while n != 0:
# 	r = n % 10
# 	sum1 = sum1+(r**b)
# 	n = n//10
# if s == sum1:
# 	print("The given number", s, "is armstrong number")
# else:
# 	print("The given number", s, "is not armstrong number")









#Python Program for Program to find area of a circle

# def findArea(r):
#     PI = 3.142
#     return PI * (r*r);
# print("Area is:", findArea(5));







#QN.Python program to print all Prime numbers in an Interval
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# The first few prime numbers are {2, 3, 5, 7, 11, ….}.

# lower = int(input("enter the lower interval:"))
# upper = int(input("enter the upper interval:"))

# for num in range(lower, upper+1):
#     if num > 1:
#         for i in range(2,num):
#             if(num%1)==0:
#                 break
#         else:
#             print(num)






# Python program to check whether a number is Prime or not
# num = 13
# if num > 1:
#     for i in range(2, int(num/2)+1):
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i)==0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")







# Python Program for n-th Fibonacci number
# n = int(input("enter how many number you want to:"))
# first=0
# second=1
# for i in range(n):
#     print(first,end=" ")
#     temp = first
#     first = second
#     second = temp+second







# Python Program for How to check if a given number is Fibonacci number?
# A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square 

# import math

# #A utility function that return true if x is perfect square

# def isPerfectSquare(x):
#     s = int(math.sqrt(x))
#     return s*s ==x

# #Return true if n is a fibonacci Number, else false

# def isFibonacci(n):
#     #n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
#     #n is a perfect square
#     return isPerfectSquare(5*n*n +4) or (5*n*n -4)

# #A utility function that test above functions

# for i in range(1,11):
#     if (isFibonacci(i)==True):
#         print(i,"is a Fibonacci number")
#     else:
#         print(i,"is not a Fibonacci number")







# Python Program for n\’th multiple of a number in Fibonacci Series

# Program to print ASCII Value of a character
#  ord() : It converts the given string of length one,
#  returns an integer representing the Unicode code point of the character.
#  For example, ord(‘a’) returns the integer 97. 

# c = 'g'
# print("The ASCII value of '" + c + "' is ", ord(c))






#Python Program for Sum of squares of first n natural numbers
# def squaresum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + i*i
#     return sum

# n = 4
# print(squaresum(n))





#Python Program for cube sum of first n natural numbers

# def cubesum(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum = sum + i*i*i
#     return sum

# n = 4
# print(cubesum(n))


















