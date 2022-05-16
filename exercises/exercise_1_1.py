"""
Add your solution to exercise 1.1 here.

Make sure the Python script is executable and has some assertions on the expected output, e.g., using `assert`.

Write a function that takes two list of integers as input and returns the integers that are in both lists as a new list.

input: [1,5,70,24,155], [17,24,25,24,68,155]
$ [24,155]

input: [5,109,49,3], [63, 1, 44, 9]
$ []

input: [1,1,1,1,1], [2,2,2,2,2,2,1]
$ [1]

"""


def matches(x: list, y: list) -> list:
    """
    Function take two list arguments
    Compare two list
    Return a list with the matching values
    """
    list_a = set(x)
    list_b = set(y)
    if list_a <= list_b:
        return [i for i in list_a if i in list_b]

    return [i for i in list_b if i in list_a]


a = [1, 5, 70, 24, 155]
b = [17, 24, 25, 24, 68, 155]

output = matches(a, b)

assert 24 in output
assert 155 in output
assert len(output) == 2

############

a = [5, 109, 49, 3]
b = [63, 1, 44, 9]

output = matches(a, b)

assert len(output) == 0

############

a = [1, 1, 1, 1, 1]
b = [2, 2, 2, 2, 2, 2, 1]

output = matches(a, b)

assert 1 in output
assert len(output) == 1
