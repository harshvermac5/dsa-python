'''Case 03:
Array of integers are sorted in ascending order, find the starting and ending position of a given number
'''

# this function takes three things as parameters
def binary_search(lo, hi, condition):
    # creates a while loop until the list gets exhausted
    while lo <= hi:
        # middle value will be the floor division of the list
        mid = (lo + hi) // 2
        # result will the store the output of the condition function, which is a parameter of this function
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            # if the result is left, in this case the query is larger than target so we have search in left portion of the list. so the ceiling of the index is reclassified
            hi = mid - 1
        else:
            # talking about the case of right, where we have search in right part of list
            lo = mid + 1
    # if loop breaks somehow, returns -1
    return -1

# function to find the first position, taking the list and the target num as parameters
def first_position(nums, target):
    # nested function that takes middle value as parameter, returns the guiding output
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return "left"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    # output of the function is then passed to parent function of binary search
    return binary_search(0, len(nums)-1, condition)


# function to find the position of the query from the last, does the same as previous function
def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid+1] == target:
                return "right"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums)-1, condition)

def first_and_last_positions(nums, target):
    return first_position(nums, target) , last_position(nums, target)

nums = [1,2,3,4,5,6,7,8,9]
target = 3

print(first_and_last_positions(nums, target))
