def binary_search(arr, target):
    left,right = 0, len(arr)-1

    while left <= right:
        midpoint = left + (right - left) // 2
        if target == arr[midpoint]:
            return midpoint
        
        elif target > arr[midpoint]:
            left = midpoint + 1

        elif target < arr[midpoint]:
            right = midpoint - 1



arr = [1,2,3,4,5,6,7,8]
     #[0,1,2,3,4,5,6,7]

target = 9

print(binary_search(arr, target))