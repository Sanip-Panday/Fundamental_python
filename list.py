#Python program to interchange first and last elements in a list
# The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].


# def swapList(newList):
#     newList[0], newList[-1] = newList[-1], newList[0]
#     return newList

# newList = [12,23,43,23,45]
# print(swapList(newList))


#  Swap the first and last element is using tuple variable.
#  Store the first and last element 
# as a pair in a tuple variable, say get, and
#  unpack those elements with first and last element in that list. Now,
#  the First and last values in that list are swapped. 

# Swap function
# def swapList(list):
	
# 	# Storing the first and last element 
# 	# as a pair in a tuple variable get
# 	get = list[-1], list[0]
	
# 	# unpacking those elements
# 	list[0], list[-1] = get
	
# 	return list
	
# # Driver code
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))





# Python program to swap two elements in a list

# Swap Two Element in a List Using temp variable

# def swapPositions(lis, pos1, pos2):
#     temp = lis[pos1]
#     lis[pos1] = lis[pos2]
#     lis[pos2] = temp
#     return lis

# list = [12,43,53,23,13]
# pos1, pos2 = 1, 3

# print(swapPositions(list, pos1-1, pos2-1))    ---->>  ??




# Swap Two Elements in a List using comma assignment 
# Python3 program to swap elements
# at given positions

# Swap function
# def swapPositions(list, pos1, pos2):
	
# 	list[pos1], list[pos2] = list[pos2], list[pos1]
# 	return list

# # Driver function
# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3

# print(swapPositions(List, pos1-1, pos2-1))










#  Python | Ways to find length of list

# list = [23,43,545,65,1,4,32,234]
# n = len(list)
# print("The lenght of list is:", n)


# li = [1,3,4,5,6]
# print("the list is:" + str(li))
# list_len = sum(1 for i in li) 
# print(list_len)











# Python | Ways to check if element exists in list

# list = [2,3,4,5,6,7]
# # checking if element 7 is present
# # in the given list or not
# i = 7
# # if element present then  return
# # exist otherwise not exist
# if i in list:
#     print("exist")
# else:
#     print("not exist")



# Find if an element exists in the list using a loop 

# list = [2,3,4,5,6,7]
# for i in list:
#     if(i == 4):
#         print("Element Exists")




# Check if an element exists in the list using any() function
# It achieves this by utilizing the any() function with a generator expression. 
# The generator expression iterates through each element test_list and checks if 
# it appears more than once in the list. The result of this check is stored in the variable result

# list1 = [1,3,4,54,6,5]
# result = any(item in list1 for item in list1)
# print("Does string contain any list element: " +str(bool(result)) )
















#--------------------> Different ways to clear a list in Python

# Clear a List using Python List clear()

# list1 = [3,5,6,7,8,9]

# print('list1 before clear:', list1)

# list1.clear()
# print('list1 after clear:', list1)




# ------------------->Clearing a Python List Using “*= 0”

# This is a lesser-known method, but this method removes all elements of the list
#  and makes it empty. In this example, we are using *=0 to clear a list.

# list1 = [1,2,3,4]
# print("List1 before clearing is: " + str(list1))

# list1 *= 0
# print("List1 after clearing is: " + str(list1))





#  ----------------------->   Python | Reversing a List
# 1.--------------> Reverse List Using Slicing Technique

# In this technique, a copy of the list is made, 
# and the list is not sorted in place. Creating a copy requires more space to hold all the existing elements.
#  This exhausts more memory. Here we are using the slicing technique to reverse our list in Python.

# def Reverse(lst):
#     new_lst = lst[::-1]
#     return new_lst

# lst = [10,20,30,40,50]
# print(Reverse(lst))



# # 2. Reverse List by Swapping Present and Last Numbers at a Time
# # If the arr[], size if the length of the array is 1, then return arr. elif length of the array is 2,
# #  swap the first and last number and return arr. otherwise, initialize i=0. Loop for i in size//2 
# # then swap the first present and last present numbers if the first and next numbers indexes are not same, 
# # then swap next and last of next numbers then increment i+=2, and after looping return arr.


# # Python program to reverse an array
# def list_reverse(arr, size):

#     # if only one element present, then return the array
#     if(size==1):
#         return arr
    
#     # if only two elements present, then swap both the numbers.
#     elif(size==2):
#         arr[0], arr[1] = arr[1], arr[0]
#         return arr
    
#     # if more than two elements presents, then swap first anad last numbers.
#     else:
#         i=0
#         while(i<size//2):

#     #swap present and preceding numbers at time and jump to second element after swap
#             arr[i],arr[size-i-1] = arr[size-i-1],arr[i]

#     #skip if present and preceding numbers indexes are same
#             if((i != i+1 and size-i-1 != size-i-2) and (i != size-i-2 and size-i-1 != i+1)):
#                 arr[i+1], arr[size-i-2] = arr[size-i-2], arr[i+1]
#             i += 2
#         return arr

# arr = [1,2,3,4,5]
# size = 5
# print('Original List:', arr)
# print("Reversed List:", list_reverse(arr,size)) 


# 3. Reverse List Using the Reversed() and Reverse() Built-In Function

# Using reversed() we can reverse the list and a list_reverseiterator object is created, 
# from which we can create a list using list() type casting. 
# Or, we can also use the list reverse() function to reverse list in place.
# lst = [1,2,3,4,5]
# # lst.reverse()
# # print("Using reverse()", lst)
# print("Using reversed()", list(reversed(lst)))






# ----------------------->Python program to find sum of elements in list

# total = 0
# list1 = [1,2,3,4,5]

# # Iterate each element in List
# # and add them in variable total
# for ele in range(0, len(list1)):
#     total = total + list1[ele]

# print("Sum of all elements in given list:", total)


# using sum() method
# list1 = [11,12,13,15,14]
# total = sum(list1)
# print("Sum of all elements in given list1 is:", total)


# Using list comprehension 
# list1 = [12,14,15,17,19]
# s = [i for i in list1]
# print(sum(s))







#------------------>     Python | Multiply all numbers in the list
# multiple = 1
# list1 = [1,2,3,4,5]
# for ele in range(0, len(list1)):
#     multiple = multiple * list1[ele]


# print("Multiple of list1:", multiple)






# Multiply all numbers in the list using numpy.prod()

# Python3 program to multiply all values in the
# list using numpy.prod()

# import numpy
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]

# # using numpy.prod() to get the multiplications
# result1 = numpy.prod(list1)
# result2 = numpy.prod(list2)
# print(result1)
# print(result2)







# ------------->    Python program to find smallest number in a list
# 1.Sorting the list to find smallest number in a list

# Here writing a Python program where we are sorting the entire list and then returning the first element as it’ll be the smallest element present in the list.
# list1 = [12,32,4,7,3,87,34]
# list1.sort()
# print("Smallest element in given list is:", list1[0])


# In Descending order

# Here we are sorting using the sort() function the entire list and then returning the last element as it’ll be the smallest element present in the list.
# list1 = [12,32,4,7,3,87,34]
# list1.sort(reverse=True)
# print("Smallest element in given list is:", list1[-1])


# Using min() Method to find smallest number in a list

# Here we are using the min Method and then returning the smallest element present in the list.
# Python program to find smallest 
# number in a list

# list of numbers
# list1 = [10, 20, 1, 45, 99]


# # printing the minimum element
# print("Smallest element is:", min(list1))


# ---------->    Python program to find largest number in a list

# list1 = [22,11,67,34,53]

# list1.sort(reverse=True)
# print("The largessst number in a list1 is:",list1[0] )

# Find Largest Number in a List Using max() method
# list1 = [10,14,20,22,24,12,54]
# print("Largest element is:", max(list1))


# Find the max list element on inputs provided by user 
# list1 = []
# # asking number of elements to put in the list
# num = int(input("Enter number of elements in list:"))

# # Iterating till num to append elemens in list
# for i in range(1, num+1):
#     ele = int(input("Element: "))
#     list1.append(ele)
# # printing the maximum element
# print("Largest element is:", max(list1))


# Find Largest Number in a List Without using built-in functions

# def myMax(list1):
#     # Assume first number in list is larger
#     # initially and assign it to variable "max"
#     max = list1[0]

# # Now traverse through the list and compare 
# # each number with "max" value. Whichever is
# # largest assign that value to max
#     for x in list1:
#         if x>max:
#             max = x
#     # after complete traversing the list 
#     # return the "max" value
#     return max

# # Driver code
# list1 = [10,12,43,23,54,32]
# print("Largest element is:", myMax(list1))


# Python program to find second largest number in a list
# list of numbers - length of 
# list should be at least 2
# list1 = [10,20,4,45,99]  
# mx = max(list1[0], list1[1])  
# secondmax = min(list1[0], list1[1])
# n = len(list1)
# for i in range(2,n):
#     if list1[i] > mx:
#         secondmax = mx
#         mx = list1[i]
#     elif list1[i] > secondmax and \
#         mx != list1[i]:
#         secondmax = list1[i]
#     elif mx == secondmax and \
#         secondmax != list1[i]:
#         secondmax = list1[i]
# print("Second highest number is: ", \
#       str(secondmax))

# --------->    Python program to find N largest elements from a list
# Given a list of integers, the task is to find N largest elements 
# assuming size of list is greater than or equal o N. 

# Examples :

# Input : [4, 5, 1, 2, 9] 
#         N = 2
# Output :  [9, 5]

# Input : [81, 52, 45, 10, 3, 2, 96] 
#         N = 3
# Output : [81, 96, 52]

# A simple solution traverse the given list N times. In every traversal,
#  find the maximum, add it to result, and remove it from the list.

# def Nmaxelements(list1, N):
#     final_list = []
    
#     for i in range(0, N):
#         max1 = 0

#         for j in range(len(list1)):
#             if list1[j] > max1:
#                 max1 = list1[j]

#         list1.remove(max1)
#         final_list.append(max1)
#     print(final_list)

# list1 = [2,3,4,5,43,53,23,64]
# N = 3
# Nmaxelements(list1, N)







#  --------> Python program to print even numbers in a list

# Method 1: Using for loop

# Iterate each element in the list using for loop and check if num % 2 == 0.
#  If the condition satisfies, then only print the number. 

# list1 = [23,32,21,35,38]
# for num in list1:
#     if num % 2 == 0:
#         print(num, end= " ")

# Method 2: Using while loop 

# list1 = [10,13,14,16,17,19,20]
# num = 0

# while(num < len(list1)):
#     if list1[num] % 2 == 0:
#         print(list1[num], end= " ")
#     num += 1

# Method 3: Using list comprehension 
# list1 = [23,32,21,35,38]
# even_nos = [num for num in list1 if num % 2 == 0]
# print("Even numbers in a list:", even_nos)




# --------->   Python program to print odd numbers in a List
# Using for loop : Iterate each element in the list using for loop and check if num % 2 != 0. 
# If the condition satisfies, then only print the number. 

# list1 = [10,13,14,16,17,19,20]
# for num in list1:
#     if num % 2 != 0:
#         print(num, end=" ")

# Using List Comprehension
# list1 = [10,13,14,16,17,19,20]
# only_odd = [num for num in list1 if num % 2 ==1]
# print(only_odd)





# ---------->    Python program to print all even numbers in a range

# Example #1: Print all even numbers from the given list using for loop Define start and end limit of range.
#  Iterate from start till the range in the list using for loop and check if num % 2 == 0. 
# If the condition satisfies, then only print the number. 

# for even_numbers in range(4,15,2):
#     print(even_numbers, end=' ')



#   Example #2: Taking range limit from user input

# start = int(input("enter the start of range: "))
# end = int(input("enter the end of range: "))

# for num in range(start, end+1):

#     if num % 2 == 0:
#         print(num, end=' ')



# ------>    Python program to print all odd numbers in a range
# Example #1
# for even_numbers in range(1,15,2):
#     print(even_numbers, end=' ')


# Example #2: Taking range limit from user input

# start = int(input("enter the start of range: "))
# end = int(input("enter the end of range: "))

# for num in range(start, end+1):

#     if num % 2 != 0:
#         print(num, end=' ')


# ---------->    Python program to print positive numbers in a list
# Example #1: Print all positive numbers from given list using for loop Iterate each element in the list
#  using for loop and check if number is greater than or equal to 0.
#  If the condition satisfies, then only print the number. 

# list1 = [23,-12,32,-32,43,-42]
# for num in list1:
#     if num >= 0:
#         print(num, end=" ")


# Example 2 : Using While loop

# list1 = [23,-12,32,-32,43,-42]
# num = 0
# while(num < len(list1)):
#     if list1[num] >= 0:
#         print(list1[num], end = ' ')
#     num += 1

# Example #3: Using list comprehension 

# list1 = [23,-12,32,-32,43,-42]
# pos_numbers = [num for num in list1 if num >= 0]
# print("Positive number:", pos_numbers)


# ------>      Remove multiple elements from a list in Python
# Example #1: Let’s say we want to delete each element in the list which is divisible by 2 or all the even numbers. 
# list1 = [2,4,5,6,11,43,53]
# for ele in list1:
#     if ele % 2 == 0:
#         list1.remove(ele)
# print("New list after removing all even numbers:", list1)



# Example #2: Using list comprehension

# Removing all even elements in a list is as good as only including all the elements which are not even( i.e. odd elements). 

# list1 = [2,4,5,6,11,43,53]
# # will create a new list, 
# # excluding all even numbers
# list1 = [elem for elem in list1 if elem % 2 != 0]
# print(*list1)



# Example #3: Remove adjacent elements using list slicing

# Below Python code remove values from index 1 to 4.
# list1 = [11, 5, 17, 18, 23, 50]
# # removes elements from index 1 to 4
# # i.e. 5, 17, 18, 23 will be deleted
# del list1[1:5]
# print(*list1)




# Example #4: Using list comprehension

# Let’s say the elements to be deleted is known, instead of the indexes of those elements.
#  In this case, we can directly eliminate those elements without caring about indexes which we will see in next example. 

# list1 = [11, 5, 17, 18, 23, 50]

# # item to be removed
# unwanted_num = {11,5}

# list1 = [ele for ele in list1 if ele not in unwanted_num]
# print("new list after removing unwanted numbers:", list1)




# Example #5: When index of elements is known.
# Though indexes of elements in known, deleting the elements randomly will change the values of indexes.
#  Hence, it is always recommended to delete the largest indices first.
#  Using this strategy, index of smaller values will not be changed.
#  We can sort the list in reverse order and delete the elements of list in descending order.

# list1 = [11, 5, 17, 18, 23, 50]
# # given index of elements 
# # removes 11, 18, 23
# unwanted = [0,3,4]

# for ele in sorted(unwanted, reverse=True):
#     del list1[ele]
# print(*list1)


# --------->    Python – Remove empty List from List
# Method 1: Using list comprehension: This is one of the ways in which this problem can be solved.
#  In this, we iterate through the list and don’t include the list which is empty. 

# test_list = [5, 23, 43, [], 43, [], 21, 50]

# # priting the original list
# print("The original list is:" + str(test_list))

# # remove empty list from list
# # using list comprehension
# res = [ele for ele in test_list if ele != []]

# # print result
# print("List after empty list removal:" + str(res))



# Method 3: Using function definition 
# def empty_list_remove(input_list):
#     new_list = []
#     for ele in input_list:
#         if ele:
#             new_list.append(ele)
#     return new_list

# input_list = [5,6, [], 3, [], [], 9]

# # print initial list values
# print(f"The original list is: {input_list}")

# # function-call and print values
# print(f"List after empty list removal: {empty_list_remove(input_list)}")
    

# --------->    Python | Cloning or Copying a list

# Copy or Clone a List Using Slicing Technique :

# def Cloning(li1):
#     li_copy = li1[:] #Thereby selecting the entire list. Hence this is a common idiom to make a copy of a list.

#     return li_copy

# li1 = [2,4,5,6,7,9]
# li2 = Cloning(li1)
# print("Original list:", li1)
# print("After Cloning:", li2)


# Clone or Copy Using Python extend() method 

# The lists can be copied into a new list by using the extend() function.
#  This appends each element of the iterable object (e.g., another list) to the end of the new list.

# def Cloning(li1):
#     li_copy = []
#     li_copy.extend(li1)
#     return li_copy

# li1 = [4,8,12,16,20]
# li2 = Cloning(li1)
# print("Original list:", li1)
# print("After Cloning:", li2)





# ------------>    Python | Count occurrences of an element in a list
# Examples: 

# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
# Output: 3 
# Explanation: 10 appears three times in given list.
# Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
# Output: 0
# Explanation: 16 appears zero times in given list.


# Python Count occurrences using a Loop in Python:

# We keep a counter that keeps on increasing if the required element is found in the list.
# def countX(lst,x):
#     count = 0
#     for ele in lst:
#         if (ele == x):
#             count = count + 1
#     return count

# lst = [2,4,5,2,6,4,2,6,4,2]
# x = 4
# print('{} has occured {} times'.format(x, countX(lst,x)))




# Python Count Occurences using List Comprehension
# list1 = [1,2,4,5,3,2,3,6,7,2]
# ele = 2
# x = [i for i in list1 if i == ele]
# print("the element" ,ele, "occurs" ,len(x), "times")


# Count occurrences of an element using count()
# def countX(lst,x):
#     return lst.count(x)

# lst = [8,6,3,6,4,7,8,5,4,3,5,6]
# x = 6
# print('{} has occured {} times'.format(x, countX(lst,x)))



#-------------->     Python | Remove empty tuples from a list
# Method 1: Using the concept of List Comprehension 

# def Remove(tuples):
#     tuples = [t for t in tuples if t]
#     return tuples

# tuples = [(), ('Ram','13','4'), ('Prashu', '23','2'), (), ('sita','24','5')]
# print(Remove(tuples))


# Method: Using while and in operator

# def Remove(tuples):
#     while () in tuples:
#         tuples.remove(());
#     return tuples

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
# print(Remove(tuples))






# ---------->    Python | Program to print duplicates from a list of integers

# Examples:

# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]

# Input :  list = [-1, 1, -1, 8]
# Output : output_list = [-1]

# Method 1: Using a single for loop

# list1 = [1,2,1,3,1,2,3,5,1,2,4,3,2,9]
# uniqueList = []
# duplicateList = []
# for i in list1:
#     if i not in uniqueList:
#         uniqueList.append(i)
#     if i not in duplicateList:
#         duplicateList.append(i)

# print(duplicateList)

# Method 2: Using Counter() function from collection module

# from collections import Counter
# l1 = [1,2,3,4,1,2,3,4,2,3,1,8,9]
# d = Counter(l1)
# print(d)

# new_list = list([item for item in d if d[item] > 1])
# print(new_list)





# --------->   Python program to find Cumulative sum of a list 
# Examples : 
 

# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]

# Input : list = [4, 10, 15, 18, 20]
# Output : [4, 14, 29, 47, 67]

# Approach 1 : 
# We will use the concept of list comprehension and list slicing to get the cumulative sum of the list. 
# The list comprehension has been used to access each element from the list and 
# slicing has been done to access the elements from start to the i+1 element.
#  We have used the sum() method to sum up the elements of the list from start to i+1.

# def Cumulative(lists):
#     cu_list = []
#     length = len(lists)
#     cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
#     return cu_list[1:] 

# lists = [10,20,30,40,50]
# print(Cumulative(lists))

# Approach 2:
# lists = [10,20,30,40,50]
# new_list = []
# j = 0
# for i in range(0, len(list)):
#     j += list[i]
#     new_list.append(j)

# print(new_list)





# Alternate approach : Use itertools module

#  One approach that is not mentioned in the provided solution is
#  to use the built-in accumulate() function from the itertools module.
#  This function allows you to perform a cumulative sum of the elements in an iterable,
#  and returns an iterator that produces the cumulative sum at each step.

# To use this function, you can pass your list as the first argument, 
# and specify the operator.add function as the second argument, which will be used to perform the cumulative sum. 
# Here is an example of how this can be implemented:


# from itertools import accumulate
# import operator

# def cumulative_sum(input_list):
#         #Use the accumulate() function to perform a cumulative sum of the elements in the list
#     cumulative_sum_iter = accumulate(input_list, operator.add)

#        # Convert the iterator to a list and return it
#     return list(cumulative_sum_iter)

# input_list = [10,20,30,40,50]
# output_list = cumulative_sum(input_list)
# print(output_list)






#  --------------> Python | Sum of number digits in List

# Method #1 : Using loop + str() 
# This is brute force method to perform this particular task. 
# In this, we run a loop for each element, convert each digit to string,
#  and perform the count of the sum of each digit.



# test_list = [10,22,30,42]
# # printing original lists
# print("Original list is: " + str(test_list))

# # Sum of number digits in list
# # Using loop + str()

# res = []
# for ele in test_list:
#     sum = 0
#     for digit in str(ele):
#         sum += int(digit)
#     res.append(sum)

# print("List integer Summation: " + str(res))



# Method #6 : Using map() function and modulo operator :

# Step-by-step algorithm for implementing the approach

# 1) First, define a function digit_sum(num) which takes a single number as input and returns the sum of its digits

#     Initialize a variable digit_sum to 0.
#     Apply a while loop to extract the last digit of the number using the modulo operator (%) and add it to the digit_sum variable.
#     Divide the number by 10 using floor division operators (//) to remove the last digit.
#     Repeat sub point 2 and 3 until the number becomes zero.
#     Return the digit_sum variable.

# 2) Define a function sum_of_digits_list(lst) which will takes a list of numbers as input
#  and returns a list containing the sum of digits of each number in the input list, using the following steps:

#     Apply map() function to the digit_sum() function.
#     Convert the resulting map object to a list using the list() function.
#     Return the resulting list.

# 3) Define a list of numbers lst which will calculate the sum of digits.

# 4) Now wecall the sum_of_digits_list(lst) function with lst as the input.

# 5) Print the resulting list.

# lst = [12,32,43,54,65]
# def digit_sum(num):
#     digit_sum = 0
#     while num > 1:
#         digit_sum += num % 10
#         num //= 10 
#     return digit_sum

# def sum_of_digits_list(lst):
#     return list(map(digit_sum, lst))

# print(sum_of_digits_list(lst))

# ------------->Break a list into chunks of size N in Python

# Method 1: Break a list into chunks of size N in Python using yield keyword

# The yield keyword enables a function to come back where it left off when it is called again.
#  This is the critical difference from a regular function.
#  A regular function cannot comes back where it left off. The yield keyword helps a function to remember its state. 

# my_list = ['sanip','mina','pratima','narayan','chitwan','bharatpur','nepal','uncle']

# # Yield sucuessive n-sized chunks from l
# def divide_chunks(l,n):

#     # looping till length l
#     for i in range(0, len(l), n):
#         yield l[i:i+n]

# # How many elements each list should have
# n = 5

# x = list(divide_chunks(my_list, n))
# print(x)



# Method 2: Break a list into chunks of size N in Python using a loop

# In this example, we are using a loop in python and list slicing that will help us to break a list into chunks.

# my_list = [1,2,3,4,5,6,7,8,9]
# start = 0
# end = len(my_list)
# step = 3
# for i in range(start,end,step):
#     x = i
#     print(my_list[x:x+step])



# ------------>    Python | Sort the values of first list using second list
# Given two lists, sort the values of one list using the second list.

# Examples: 

#     Input : list1 = [“a”, “b”, “c”, “d”, “e”, “f”, “g”, “h”, “i”]
#                list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
#     Output : [‘a’, ‘d’, ‘h’, ‘b’, ‘c’, ‘e’, ‘i’, ‘f’, ‘g’]

#     Input : list1 = [“g”, “e”, “e”, “k”, “s”, “f”, “o”, “r”, “g”, “e”, “e”, “k”, “s”]
#                 list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
#     Output : [‘g’, ‘k’, ‘r’, ‘e’, ‘e’, ‘g’, ‘s’, ‘f’, ‘o’]



# Approach : 
 

#     Zip the two lists.
#     Create a new, sorted list based on the zip using sorted().
#     Using a list comprehension extract the first elements of each pair from the sorted, zipped list.

# Concept : 
# The purpose of zip() is to map a similar index of multiple containers so that they can be used just using as a single entity.


# def sort_list(list1, list2):
#     zipped_pairs = zip(list2, list1)
#     z = [x for _, x in sorted(zipped_pairs)]
#     return z

# x = ["a", "b", "c", "d", "e", "f", "g"]
# y = [0,2,1,1,3,4,2]
# print(sort_list(x, y))








       















