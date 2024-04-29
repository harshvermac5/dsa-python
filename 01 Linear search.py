# we are writing a program to find the index of a given number in the list of number arranged in descending order

# this function was failing when list is empty, so it throws the out of range error
'''def locate_card(cards, query):
    position = 0
    
    print("cards:", cards)
    print("query:", query)

    while True:
        print("position:", position)
        if cards[position] == query:
            return position
        position += 1

        if position == len(cards): # in case when list is exhausted
            return -1
    pass'''

def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

# test is a dictionary that contain two keys, input and output. input is a nested dictionary which contain two keys cards and query where cards is a list while query is a constant value
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
        "cards": [8,8,6,4,2,3,5,6,7,8,8,9],
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