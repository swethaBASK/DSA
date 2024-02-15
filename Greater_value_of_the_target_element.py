def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    i = 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Iteration no: {i}")
        print(f"low = {low} ---> mid = {mid} ---> high = {high}\n")
        if arr[mid] == target: 
            return (arr[mid+1])
        elif arr[mid] > target:
            if arr[mid-1]<target:
                print(arr[mid])
            
            high = mid - 1
        else:
            low = mid + 1
        i += 1
            
    return -1
    
    
    
arr = [3,8,18,39,99]
target = 5
idx = binary_search(arr, target)
    
