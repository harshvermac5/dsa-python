# this code is great, but is failing to address the scenario of getting first number as index
'''def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi: # lo, hi and mid are indexes and ultimately mid is being returned
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        print("lo: ", lo, "hi: ", hi, "mid: ", mid, "mid number: ", mid_number, "query:", query)

        if mid_number == query:
            return mid # remember in this case, hi represents the last of the index, a smaller number
        elif mid_number < query: # when mid number is smaller than the query, assign one number smaller to hi
            hi = mid-1
        elif mid_number > query:
            lo = mid + 1

    return -1
'''
def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:",mid, "mid number:", mid_number)
    if mid_number == query:
        # verifying whether the number before the query is equal to the mid value or not
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"
    
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo:",lo, "hi:", hi, "query:", query)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

test = {
    "input": {
        "cards" : [13, 11, 10, 7, 4, 3, 1, 0],
        "query" : 7
    },
    "output" : 3
}

# the line below access the value of both the keys inside of test dictionary, compares it and outputs the binary 


tests = []

# query occurs in middle
tests.append(test)

# query occurs in almost last of the list
tests.append({
    "input" : {
        "cards" : [13,11,10,7,4,3,1,0],
        "query" : 1
    },
    "output":6
})

# query is the first element
tests.append({
    "input" : {
        "cards" : [1,13,11,10,7,4,3,0],
        "query" : 1
    },
    "output":0
})

# query is the last element
tests.append({
    "input" : {
        "cards" : [3, -1, -8, -127],
        "query" : -127
    },
    "output" : 3
})

# cards contains only one element
tests.append({
    "input" : {
        "cards" : [5],
        "query" : 5
    },
    "output" : 0
})

# cards doen't contain query
tests.append({
    "input" : {
        "cards" : [9,7,5,2,-9],
        "query" : 4
    },
    "output" : -1
})

# cards is empty
tests.append({
    "input" : {
        "cards": [],
        "query": 7
    },
    "output" : -1
})

# numbers in cards are repeating, but query is not
tests.append({
    "input": {
        "cards": [9,7,5,4,4,4,3,2,1,1],
        "query": 3
    },
    "output": 7
})

# numbers in cards are repeating, alongwith query
tests.append({
    "input": {
        "cards": [8,8,6,3,3,3,3,5,6,7,8,8,9],
        "query": 3
    },
    "output": 3
})

# print(tests)
for test in tests:
    print(locate_card(**test["input"]) == test["output"])