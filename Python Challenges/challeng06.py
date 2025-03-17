#Binary Search: Write a program that implements binary search.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


######## Solution 2 by Negar Deilami 3.15.25 

def binarySearch(targetvalue,list1):
    list2 = list1
    list1.sort()
    max = list1[-1]
    min = list1[0]
    while min <= targetvalue <= max :
        if list1[int(len(list1)/2)] > targetvalue :
            list1 = list1[:len(list1)//2]
            if list1[-1] < targetvalue:
             return(print('Target not found'))
        elif list1[int(len(list1)/2)] < targetvalue :
            list1 = list1[len(list1)//2:]
            if list1[0] > targetvalue:
                return(print('Target not found'))
        elif targetvalue == list1[int(len(list1)/2)]:
          return(print('the Target Value is positioned in array', list2.index(targetvalue)))
    else :
         return(print('Target is not within range'))

binarySearch(12,[2,3,4,1,7])


