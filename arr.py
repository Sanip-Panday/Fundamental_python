# Python Program to find sum of array

# def _sum(arr):
#     sum = 0
#     for i in arr:
#         sum = sum + i
#     return(sum)

# if __name__ == "__main__":
#     arr = [1,2,3,4]
#     n = len(arr)
#     ans = _sum(arr)
#     print("sum of array is:", ans)




# Python Program to find largest element in an array
# To find the largest element in an array, iterate over each element 
# and compare it with the current largest element. If an element is greater, update the largest element. 
# At the end of the iteration, the largest element will be found.


# def largest(arr, n):
#     # Initialize maximum element
#     max = arr[0]

#     # Traverse array elements from second
#     # and compare every element with 
#     # current max
#     for i in range(1, n):
#         if arr[i] > max:
#             max = arr[i]
#     return max

# #Driver Code
# arr = [10,345,22,334,322,553]
# n = len(arr)
# ans = largest(arr, n)
# print("Largest in given array ", ans)



# Python Program for array rotation


# 1) Reverse the entire list by swapping first and last numbers

#    i.e start=0, end=size-1

# 2) Partition the first subarray and reverse the first subarray, by swapping first and last numbers.

#    i.e start=0, end=size-d-1

# 3) Partition the second subarray and reverse the second subarray, by swapping first and last numbers.

#    i.e start=size-d, end=size-1
















# Python Program for Reversal algorithm for array rotation





#  Python Program to Split the array and add the first part to the end
# 
# Input : arr[] = {12, 10, 5, 6, 52, 36}
#             k = 2
# Output : arr[] = {5, 6, 52, 36, 12, 10}
# Explanation : Split from index 2 and first 
# part {12, 10} add to the end .


# def splitArr(arr, n, k):
#     for i in range(0, k):
#         x = arr[0]
#         for j in range(0, n-1):
#             arr[j] = arr[j + 1]

#         arr[n-1] = x

# arr = [12,10,5,6,54,45]
# n = len(arr)
# position = 2
# splitArr(arr, n, position)

# for i in range(0, n):
#     print(arr[i], end= ' ')











#Python Program for Find reminder of array multiplication divided by n


# Input: arr[] = {100, 10, 5, 25, 35, 14},
# n = 11
# Output: 9
# Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9


# def findRemainder(arr, len, n):
#     product = 1
#     for i in range(len):
#         product = product * arr[i]
#     return product % n


# arr = [100,23,43,53,53]
# len =len(arr)
# n = 11
# print(findRemainder(arr, len, n))










# Python Program to check if given array is Monotonic

#  An array is monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone increasing if for all i <= j, A[i] <= A[j]. 

# An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. 

# Return Type: Boolean value, “True” if the given array A is monotonic else return “False” (without quotes). 

# Approach : Using extend() and sort()

#     First copy the given array into two different arrays using extend()
#     Sort the first array in ascending order using sort()
#     Sort the second array in descending order using sort(reverse=True)
#     If the given array is equal to any of the two arrays then the array is monotonic

# def isMonotonic(A):
#     x, y = [], []
#     x.extend(A)
#     y.extend(A)
#     x.sort()
#     y.sort(reverse=True)
#     if(x == A or y == A):
#         return True
#     return False


# A = [6, 5, 4, 4]
# print(isMonotonic(A))


