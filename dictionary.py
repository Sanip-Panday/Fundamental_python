

# PYTHON DICTIONARY METHODS:
# clear() 
# The clear() method remove all items from the dictionary.

#  copy(),
# The copy() method returns a shallow copy of the dictionary. 
# changes to the copy of the dictionary do not affect the original dictionary. 
# my_dict = {'name': 'prashuram', 'age': 24}
# new_dict = my_dict.copy()
# new_dict['age'] = 30
# print(my_dict)
# print(new_dict)





#  Get()
# The get() method returns the value of the specified key. If the key is not present in the dictionary, it will return None
# my_dict = {'name': 'prashuram', 'age': 24}
# age = my_dict.get('age')
# # print(age)   #output: 24

# # trying to get a value for a key that does not exist
# occupation = my_dict.get('occupation')
# # print(occupation) #output: None

# # setting a default value if the key does not exist
# occupation  = my_dict.get('occupation', 'student')
# # print(occupation)





#  items()
# THe items() method returns a list of key-value pairs in the dictionary
# my_dict = {'name': 'prashuram', 'age': 24}
# items = my_dict.items()
# print(items)




# keys()
# The keys() method returns a list of keys in the dictionary. 
# my_dict = {'name': 'prashuram', 'age': 24}
# keys = my_dict.keys()
# print(keys)



#  Popitem(), 
# The popitem() method removes the item that was last inserted into the dictionary.
#  In versions before 3.7, the popitem() method removes a random item.
# my_dict = {'name': 'prashuram', 'age': 24}
# print(my_dict)
# new_dict = my_dict.popitem()
# print(new_dict)




# values()
# The values() method returns a list of values in the dictionary. 
# my_dict = {'name': 'prashuram', 'age': 24}
# values = my_dict.values()
# print(values)




#  pop()
# The pop() method removes and returns the value of the specified key. If the key does not exist, 
# it raises a KeyError. To avoid this, you can pass a default value to be returned if the key is not found. 
# my_dict = {'name': 'prashuram', 'age': 24}
# age = my_dict.pop('age')
# print(age) #output 24
# print(my_dict)


 
#  update()
# The update() method updates the dictionary with the specified key-value pairs. 
# my_dict = {'name': 'prashuram', 'age': 24, 'county': 'nepal'}
# my_dict.update({'age': 23})
# print(my_dict)




#  setdefault()
# The setdefault() method returns the value of the specified key 
# my_dict = {'name': 'prashuram', 'age': 24}
# county = my_dict.setdefault('county', 'Nepal')
# print(county)
# print(my_dict)





# --------------->    Python – Extract Unique values dictionary values    ----------------------------------------->

# Extract Unique values dictionary values Using sorted() + set comprehension + values()

# test_dict = {'abc': [4,5,2], 'def':[3,4,5], 'ghi':[1,2,3]}

# # print the original dictionary
# print("The original dictionary is: " +str(test_dict))

# # extract Unique values dictionary value
# # using set comprehension + values() + sorted()

# res = list(sorted({ele for val in test_dict.values() for ele in val}))

# # printing the result
# print("The unique values list is:", res)



# Extract Unique values dictionary values Using extend() and sort() methods
# test_dict = {'abc': [4,5,2], 'def':[3,4,5], 'ghi':[1,2,3]}

# print("The original dictionary is: " +str(test_dict))

# x = list(test_dict.values())
# y= []
# res = []
# for i in x:
#     y.extend(i)
# for i in y:
#     if i not in res:
#         res.append(i)
# res.sort()

# print("The unique values is: ", str(res))


# Extract Unique values dictionary values Using Counter(),append() and sort() methods

# ALGORITHM

    # Import the Counter class from the collections module.
    # Define a dictionary test_dict with string keys and lists of integers as values.
    # Print the original dictionary.
    # Create an empty list called valuesList.
    # Iterate over the dictionary using the items() method to access the keys and values. For each key-value pair, iterate over the values list and append each value to valuesList.
    # Use the Counter() function to count the frequency of each value in valuesList. This creates a dictionary where the keys are the unique values in valuesList and the values are their frequencies.
    # Use the keys() method to extract a list of the unique values from freq.
    # Sort the uniqueValues list in ascending order.
    # Print the final list of unique values

# from collections import Counter
# test_dict = {'abc': [4,5,2], 'def':[3,4,5], 'ghi':[1,2,3]}
# print("The original dictionary is: " +str(test_dict))

# valuesList = []
# for key, values in test_dict.items():
#     for value in values:
#         valuesList.append(value)
# freq = Counter(valuesList)
# uniqueValues = list(freq.keys())
# uniqueValues.sort()

# print("The unique values is: ", str(uniqueValues))




# --------------->    Python program to find the sum of all items in a dictionary  ---------------->
# Method #1: Using Inbuilt sum() Function
# def returnSum(mydict):
#     list = []
#     for i in mydict:
#         list.append(mydict[i])
#     final= sum(list)

#     return final

# dict = {'a': 100, 'b': 200, 'c': 300}
# print("Sum: ", returnSum(dict))

# Method #2: Using For loop to iterate through values using values() function
# def returnSum(dict):
#     sum = 0
#     for i in dict.values():
#         sum = sum + i
    
#     return sum

# dict = {'a': 100, 'b':200, 'c': 300}
# print("Sum: ", returnSum(dict))


# Method #3: Using for loop to iterate over each value in a dictionary

# def returnSum(dict):
#     sum = 0
#     for i in dict:
#         sum = sum + dict[i]

#     return sum

# dict = {'a': 100, 'b':200, 'c': 300}
# print("Sum: ", returnSum(dict))



# Method #4: Using values() and sum() function
# def returnSum(dict):
#     return sum(dict.values())

# dict = {'a': 100, 'b':200, 'c': 300}
# print("Sum: ", returnSum(dict))


# Method #5: Using a generator expression and the built-in sum function
# def returnSum(myDict):
#     return sum(myDict[key] for key in myDict)

# dict = {'a': 100, 'b':200, 'c': 300}
# print("Sum: ", returnSum(dict))


# ----------> Python | Ways to remove a key from dictionary-------------------->
# Method 1: Remove a Key from a Dictionary using the del

# The del keyword can be used to in-place delete the key that is present in the dictionary in Python.
#  One drawback that can be thought of using this is that it raises an exception if the key is not found and hence non-existence of the key has to be handled.
# my_dict = {'name': 'Prashuram', 'age': 24, 'country': 'Nepal'}
# print("The dictionary before performing remove is: ", my_dict)

# # using del to remove a dict
# del my_dict['age']

# print("The dictionary after performing remove is: ", my_dict)

# # using del to remove a dict 
# # raises exception
# del my_dict['age']




# Method 2: Remove a Key from a Dictionary using pop() 
# my_dict = {'name': 'Prashuram', 'age': 24, 'country': 'Nepal'}
# print("The dictionary before performing remove is: ", str(my_dict))

# removed_value = my_dict.pop('age')
# print("The dictionary after performing remove is: ", str(my_dict)) 


# Method 3: Using items() + dict comprehension to Remove a Key from a Dictionary

# Method 4: Use a Python Dictionary Comprehension to Remove a Key from a Dictionary
# my_dict = {'name': 'Prashuram', 'age': 24, 'country': 'Nepal'}
# print("The dictionary before performing remove is: ", str(my_dict))

# a_dict = {key: my_dict[key] for key in my_dict if key != 'age'}

# print("The dictionary after performing remove is: ", a_dict)



# ----------->    Ways to sort list of dictionaries by values in Python – Using itemgetter------???????????

# What is Itemgetter in Python?

# The Itemgetter can be used instead of the lambda function to achieve similar functionality.
#  Outputs in the same way as sorted() and lambda, but has different internal implementation.
#  It takes the keys of dictionaries and converts them into tuples. 
# It reduces overhead and is faster and more efficient.
#  The “operator” module has to be imported for its work

# from operator import itemgetter

# list = [{"name": "Prashuram", "age": 24}, {"name": "Pandey", "age": 20}], {"name": "Sandy", "age": 21}

# # using sorted and itemgetter to print list sorted by age
# print("The list printed sorting by age: ")
# print (sorted(list, key = itemgetter('age')))
# print("\r")

# # using sorted and itemgetter to print list sorted by age and name
# print("The list printed sorting by age and name: ")
# print (sorted(list, key = itemgetter('age', 'name')))
# print("\r")


# # using sorted and itemgetter to print list
# # sorted by age in descending order
# print("The list printed sorting by age in descending order: ")
# print (sorted(list, key=itemgetter('age'), reverse=True) )



# ------------>    Ways to sort list of dictionaries by values in Python – Using lambda function

# list = [{"name": "Prashuram", "age": 24}, {"name": "Pandey", "age": 20}], {"name": "Sandy", "age": 21}

# # using sorted and lambda to print list sorted by age
# print("The list printed sorting by age: ")
# print (sorted(list, key = lambda i: i['age']))
# print("\r")

# # # using sorted and lambda to print list sorted by age and name
# print("The list printed sorting by age and name: ")
# print (sorted(list, key = lambda i: (i['age'], i['name'])))
# print("\r")


# # # using sorted and itemgetter to print list
# # # sorted by age in descending order
# print("The list printed sorting by age in descending order: ")
# print (sorted(list, key=lambda i: i['age'], reverse=True) )



# ---------------->    Python | Merging two Dictionaries

# Python Merge Dictionaries Using | in Python 3.9

# In the latest update of python now we can use “|” operator to merge two dictionaries. It is a very convenient method to merge dictionaries. In this example, we are using | operator to merge two dictionaries.
# def Merge(dict1, dict2):
#     res = dict1 | dict2
#     return res

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict3 = Merge(dict1, dict2)
# print(dict3)



# Python update()

# By using the method update() in Python, one list can be merged into another.
#  But in this, the second list is merged into the first list and no new list is created.
#  It returns None. In this example, we are using the update function to merge two dictionaries.

# def Merge(dic1,dic2):
#     return (dic2.update(dic1))

# dic1 = {'a': 1, 'b': 2}
# dic2 = {'c': 3, 'd': 4}

# # This returns None
# print(Merge(dic1, dic2))

# # changes made in dict2
# print(dic2)


# Python unpacking operator

# Using ** [double star] is a shortcut that allows you to pass multiple arguments to a function directly using a dictionary. 
# For more information refer **kwargs in Python. 
# Using this we first pass all the elements of the first dictionary into the third one 
# and then pass the second dictionary into the third. This will replace the duplicate keys of the first dictionary.

# def Merge(dict1, dict2):
#     res = {**dict1, **dict2}
#     return res

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict3 = Merge(dict1, dict2)
# print(dict3)




# ----------------->    Python – Convert key-values list to flat dictionary
# Sometimes, while working with Python dictionaries, we can have a problem in which we need to flatten dictionary of key-value pair pairing the equal index elements together. 


# Convert key-values list to flat dictionary Using a dictionary comprehension


# This method iterates over the indices of the ‘month’ list, and for each index i,
#  it creates a key-value pair in the new dictionary where the key is the i-th element of the ‘month’ list,
#  and the value is the i-th element of the ‘name’ list.

# dict1 = {'month': [1,2,3], 'name': ['jan', 'feb', 'march']}
# res = {dict1['month'][i]: dict1['name'][i] for i in range(len(dict1['month']))}

# print(res)





# Convert key-values list to flat dictionary using zip() + dict()

# The combination of above functions can be used to achieve the required task.
#  In this, we perform the pairing using zip() and dict() is used to convert 
# tuple data returned by zip() to dictionary format. 

# from itertools import product
# # initializing dictionary
# dict1 = {'month': [1,2,3], 'name': ['jan', 'feb', 'march']}

# print("The original dictionary is: ", str(dict1))

# # Convert key-values list ot flat dictionary
# # Using dict() + zip()
# res = dict(zip(dict1['month'], dict1['name']))

# print("Flattened dictionary: ", str(res))




# Convert key-values list to flat dictionary Using values() and dict() methods
# dict1 = {'month': [1,2,3], 'name': ['jan', 'feb', 'march']}
# print("The original dictionary is: ", str(dict1))

# # Convert key-values list ot flat dictionary
# x = list(dict1.values())
# a  =x[0]
# b = x[1]
# d = dict()
# for i in range (0, len(a)):
#     d[a[i]] = b[i]

# print("Flattened dictionary: " + str(d))





# --------->    Python – Insertion at the beginning in OrderedDict

# An OrderedDict is a dictionary subclass that remembers the order in which keys were first inserted. 
# `OrderedDict` maintains the sequence in which keys are added, ensuring that the order is preserved during iteration. 

# Input: 
# original_dict = {'a':1, 'b':2}
# item to be inserted ('c', 3)

# Output:  {'c':3, 'a':1, 'b':2}


# Method #1: Using OrderedDict.move_to_end() 

# from collections import OrderedDict

# # Initialising ordered_dict
# iniodered_dict = OrderedDict([('Prashuram', '1'), ('Pandey', '2')])

# # Inserting items in starting of dict
# iniodered_dict.update({'Mina': '3'})
# iniodered_dict.move_to_end('Mina', last = False)     #last = False to inserted at begin 

# print("Resultant Dictionary:" + str(iniodered_dict))



# Method #2: Using Naive Approach

# This method only works in case of unique keys 






# Method #3: Using OrderedDict.popitem() 

# To add a new key-value pair at the beginning of an OrderedDict, we can use popitem() method with a new OrderedDict.
#  This method returns and removes the last key-value pair in the OrderedDict.
#  We can keep popping the last key-value pair and adding it to a new OrderedDict until we get the desired order of insertion.

# from collections import OrderedDict

# # Initialising ordered_dict
# ini_dict = OrderedDict([('Prashuram', '1'), ('Pandey', '2')])

# # Creating a iniordered ordered dict
# iniodered_dict = OrderedDict()

# # Inserting new key-value pair at the beginnning of iniordered_dict
# iniodered_dict.update({'manjeet': '3'})
# iniodered_dict.move_to_end('manjeet', last=False)

# # popitem() method to remove and insert key-value pair at beginning 
# while ini_dict:
#     iniodered_dict.update({ini_dict.popitem(last=False)})


# print("Resultant Dictionary: " + str(iniodered_dict))







# ----------->    Python | Check order of character in string using OrderedDict( )
# Input: 
# string = "engineers rock"
# pattern = "er";
# Output: true
# Explanation: 
# All 'e' in the input string are before all 'r'.

# Input: 
# string = "engineers rock"
# pattern = "gsr";
# Output: false
# Explanation:
# There are one 'r' before 's' in the input string.




    # Create an OrderedDict of input string which contains characters of input strings as Key only.
    # Now set a pointer at the start of pattern string.
    # Now traverse generated OrderedDict and match keys with individual character of pattern string, if key and character matches with each other then increment pointer by 1.
    # If pointer of pattern reaches it’s end that means string follows order of characters defined by a pattern otherwise not.


# from collections import OrderedDict

# def checkOrder(input, pattern):
#     # check empty OrderedDict
#     # output will be like {'a': None, 'b': None}
#     dict = OrderedDict.fromkeys(input)
    
#     # traverse generated OrderedDict parallel with pattern string to check if order of characters are same or not. 
#     ptrlen = 0
#     for key, value in dict.items():
#         if (key == pattern[ptrlen]):
#             ptrlen = ptrlen + 1
        
#         # check if we have traverse complete pattern string
#         if (ptrlen == (len(pattern))):
#             return 'true'
        
#     # if we came out from for loop that means order was mismatched
#     return 'false'


# # Driver program
# if __name__ == "__main__":
#     input = 'engineers english'
#     pattern = 'er'
#     print(checkOrder(input, pattern))




# Check order of character in string Using two pointers

# This Approach checks if the characters in the given pattern appear in the same order in the given string.
#  It uses two pointers to keep track of the positions of the characters being compared.
#  If all the characters in the pattern are found in the same order in the string, the function returns True, otherwise False.

# Algorithm

# 1. Initialize two pointers, one for the string and one for the pattern, both starting at 0.
# 2. Traverse through the string character by character.
# 3. If the current character in the string matches the current character in the pattern, increment the pattern pointer.
# 4. Increment the string pointer after processing each character.
# 5. If the pattern pointer is equal to the length of the pattern, return True.
# 6. If the end of the string is reached and the pattern pointer is less than the length of the pattern, return False.

# def check_order(string, pattern):
#     i, j = 0, 0
#     for char in string:
#         if char == pattern[j]:
#             j += 1
#         if j == len(pattern):
#             return  True
#         i += 1

#     return False

# string = 'engineers rock'
# pattern = 'er'
# print(check_order(string, pattern))






# -------------->    Dictionary and counter in Python to find winner of election



