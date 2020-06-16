def bs(arr, target):
    return binary_search(arr, target, 0, len(arr) -1)


# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    if start == end:
        return arr[start] == target
    
    else:
        
        split = len(arr) // 2
        
        left = arr[:split]
        right = arr[split:]
        
        return (binary_search(left, target, 0, len(left) -1)) or (binary_search(right, target, 0, len(right) -1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

