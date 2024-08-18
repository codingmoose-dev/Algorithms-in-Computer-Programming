# Binary search is an efficient algorithm for finding a target value within a sorted array.
# Time Complexity - O(log n)

def BinarySearch(Array, Search_value):
    left = 0
    right = len(Array) - 1

    # With each iteration, half the values are eliminated
    while left <= right : 
        mid = (left + right) // 2
        if Array[mid] == Search_value: return mid
        elif Array[mid] > Search_value: right = mid - 1
        else: left = mid + 1
    return -1
    

myArray = [0,1,3,6,11,12,14,17,18,22,25,33,34,35,38,40,41,41,47, 50]
TargetValue = 6
SearchResult = BinarySearch(myArray, TargetValue)
# Shorthand If ... Else
print(f"Element found at index {SearchResult}!") if SearchResult != -1 else print("Element not found!") 
