def count_rotations_binary(nums):
    if not nums:  # Handle empty list
        return 0

    if len(nums) == 1:  # Handle single element list
        return 0
    
    if nums[0] < nums[-1]: # Check is list is already sorted
        return 0

    low = 0
    high = len(nums) - 1

    while low <= high: # looping until the list is exhausted
        mid = (low + high) // 2
        mid_val = nums[mid]
        first_val = nums[0]
        last_val = nums[-1]

        # Handle edge cases for binary search
        if mid == 0 or mid == len(nums) - 1:
            return mid

        # arr = [5, 6, 7, 0, 1, 2, 3, 4] mid = 3 (7//2) and mid_val = 0 which satisfy the both condition
        if mid_val <= nums[mid - 1] and mid_val <= nums[mid + 1]:
            return mid

        # arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] mid = 4 mid_value = 8 which is way larger than first_val = 4 hence rotation is in the right half of the list
        if mid_val >= first_val:
            low = mid + 1

        # arr = [7, 8, 1, 2, 3, 4, 5, 6] mid = 3, mid_value = 2 which is way smaller than the large value hence the rotation is in the left half of the list
        elif mid_val <= last_val:
            high = mid - 1

    return 0  # Return zero if no rotation was found

# Test cases
test0 = {"input": {"nums": [19,25,29,3,5,6,7,9,11]}, "output": 3}
test1 = {"input": {"nums": [4,5,6,7,8,1,2,3]}, "output": 5}
test2 = {"input": {"nums": [1,2,3,4,5,6,7]}, "output": 0}
test3 = {"input": {"nums": [7,1,2,3,4,5,6]}, "output": 1}
test4 = {"input": {"nums": [3,4,5,6,7,1,2]}, "output": 5}  # Additional test case
test5 = {"input": {"nums": []}, "output": 0}
test6 = {"input": {"nums": [1]}, "output": 0}
test7 = {"input": {"nums": [5]}, "output": 0}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]

for i, test in enumerate(tests):
    result = count_rotations_binary(**test["input"])
    expected_output = test["output"]
    print(f"Test {i}: {result == expected_output}")
