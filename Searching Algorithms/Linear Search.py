# Linear Search or Sequential Search is for finding an element within a list
# It sequentially checks each element until a match is found or the whole list has been searched
# Time Complexity O(n)

def LinearSearch(Array, Search_value):
    for index in range(len(Array) - 1):
        if Array[index] == Search_value: return index

    return -1

myArray = [0,1,3,6,11,12,14,17,18,22,25,33,34,35,38,40,41,41,47, 50]
TargetValue = 6
SearchResult = LinearSearch(myArray, TargetValue)
#Shorthand If ... Else
print(f"Element found at index {SearchResult}!") if SearchResult != -1 else print(f"Element not found!")