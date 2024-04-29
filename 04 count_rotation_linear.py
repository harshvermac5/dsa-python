# function to count the rotation of the elements
def count_rotations_linear(nums):
    position = 0 # starting the initial counter

    while position < len(nums): # loop until the list gets exhausted
        if position > 0 and nums[position] < nums[position-1]: # both condition, position has to more than zero, and previous number must be larger than the upcoming number should be satisfied. More than zero because if zero, there would be no number behind it to compare the current with.
            return position # returning position will tell the times of rotation
        position += 1

    return 0

# a list of size 9 rotated 3 times
test0 = {
    "input": {
        "nums" : [19,25,29,3,5,6,7,9,11],
    },
    "output": 3
}

# list of size 8 rotated 5 times
test1 = {
    "input": {
        "nums": [4,5,6,7,8,1,2,3]
    },
    "output": 5
}

# a list that was not rotated at all
test2 = {
    "input": {
        "nums": [1,2,3,4,5,6,7]
    },
    "output": 0
}

# a list that was rotated just once
test3 = {
    "input": {
        "nums": [7,1,2,3,4,5,6]
    },
    "output": 1
}

# a list that was rotated n-1 times
test4 = {
    "input": {
        "nums": []
    },
    "output": 0
}

# a list that was rotated n times
test5 = {
    "input": {
        "nums": [1,2,3,4,5]
    },
    "output": 0
}

# a list that is empty
test6 = {
    "input": {
        "nums": []
    },
    "output": 0
}

# a list that contains only one element
test7 = {
    "input": {
        "nums": [5]
    },
    "output": 0
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]

for i, test in enumerate(tests):
    result = count_rotations_linear(**test["input"])
    expected_output = test["output"]
    print(f"Test {i}: {result == expected_output}")
