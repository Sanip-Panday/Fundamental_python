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
