# Starting with linear search

print ("------------This is a linear search ------------" )



def linear_search(arr, target) :
    for i in range(len(arr)):
        print(f" Checking index {i}, value {arr[i]}") 
        if arr[i] == target:
            print("Match Found")
            return i
        print ("No match found")
        return -1
    
    marks = [20,30,40,10,11,13]
    target = 40
    result = linear_search (marks, target)

    if result !=-1:
        print(f"Target found at index {result}")
    else:
        print("Target not found")