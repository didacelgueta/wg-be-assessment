"""
Add your solution to exercise 1.2 here.

Make sure the Python script is executable and has some assertions on the expected output, e.g., using `assert`.

Given a list of Customers instances, where a customer is defined by a name, an email and an age, write a function that takes a list of customer instances as input and returns all groups of customers with the same age.

Given customers (name - email - age):

Joe     joe@wegroup.be      47
Sara    sara@wegroup.be     23
Alice   alice@wegroup.be    23
Bob     bob@wegroup.be      47
Gary    gary@wegroup.be     33

Expected output:
$ {23: ['Alice', 'Sara'], 33: ['Gary'], 47: ['Bob', 'Joe']}
"""


class Customer:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    """
    This class is not complete.
    You'll probably need to add some functionality to complete at least asignment 1.2.2
    """


def group_customers_by_age_1_2_1(customers):
    # Exercise 1.2.1: Add your solution without extra imports here
    pass


def group_customers_by_age_1_2_2(customers):
    # Exercise 1.2.2: Add your solution with extra imports here (tip: use an iterator from `itertools`).
    pass


if __name__ == "__main__":
    output = {23: ["Alice", "Sara"], 47: ["Bob", "Joe"], 33: ["Gary"]}
    input = [
        Customer("Joe", "joe@wegroup.be", 47),
        Customer("Sara", "sara@wegroup.be", 23),
        Customer("Alice", "alice@wegroup.be", 23),
        Customer("Bob", "bob@wegroup.be", 47),
        Customer("Gary", "gary@wegroup.be", 33),
    ]

    assert group_customers_by_age_1_2_1(input) == output
    assert group_customers_by_age_1_2_2(input) == output
