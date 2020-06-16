# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    ret_arr = []
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            ret_arr.append(arrA.pop(0))
        else:
            ret_arr.append(arrB.pop(0))
            
    ret_arr = ret_arr + arrA + arrB

    return ret_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    if len(arr) > 1:
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        return merge(left, right)
    
    else:
        return arr
    
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

