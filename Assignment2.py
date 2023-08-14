# CSCI 220/620
# Summer 2022
# Assignment 2 - Sets and Functions
# Emily Haller


import itertools
from itertools import product


# part 1
def f0_same(x):
    return x


def f1_next(x):
    return x+1


def f2_prev(x):
    return x-1


def f3_double(x):
    return x*2


def f4_alt(x):
    return x-1 if x % 2 == 1 else x+1


def get_function_type(func, func_domain, func_co_domain):
    func_range = set ()
    for element in func_domain:
        val = func(element)
        if val not in func_co_domain: # if function evaluates to something outside co-domain
            return "partial and not total"
        else:
            func_range.add(val)
    if len(func_domain) == len(func_co_domain) and len(func_range) == len(func_co_domain):
        return "bijection (one to one and onto)"
    elif func_range == func_co_domain:
        return "surjection (onto and not one-to-one)"
    elif len(func_domain) == len(func_range):
        return "injection (one to one and not onto)"
    else:
        return "nothing special"


# part 2: define operation functions
#https://www.programiz.com/python-programming/methods/set/intersection
def set_union(set1, set2):
    return set1 | set2


#https://www.pythontutorial.net/python-basics/python-set-union/
def set_intersection(set1, set2):
    return set1.intersection(set2)


#https://www.geeksforgeeks.org/python-set-difference/
def set_difference(set1, set2):
    return set1.difference(set2)


#https://www.programiz.com/python-programming/methods/set/symmetric_difference
def set_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)


#https://www.tutorialspoint.com/python-program-to-find-cartesian-product-of-two-lists
def set_cartesian_product(set1, set2):
    return list(product(set1, set2))


#https://www.codingem.com/python-how-to-get-all-combinations-of-a-list/
def set_power_set(set1):
    combinations = [] # combinations starts off as an empty set
    for r in range(len(set1) + 1): # need to iterate to get multiple lengths of combinations
        for combination in itertools.combinations(set1, r):
            combinations.append(combination) # add each combination of set1 to the combinations set
    return combinations

#part 3: list of binary numbers in range of 0 to 1, generate a number not in the list (Cantors theorem)
def flip_binary_digit(digit):
    return "1" if digit == "0" else "0"


def generate_new_number(binary_numbers):
    max_size = max([len(number) - 2 for number in binary_numbers])
    new_number = "0."
    for index in range(len(binary_numbers)):
        if index >= max_size:
            new_number += "1"  #if exceed max size then theres an imaginary zero at end of the number and flip it to get a 1
        else:
            new_number += flip_binary_digit(binary_numbers[index][index+2])
    return new_number


# part 4: define sum functions
def sum_geometric_series(a, r, n):
    if r != 1:
        return (a*(r**(n+1))-a)/(r-1)
    else:
        return (n+1)*a


def sum_arithmetic_series(n, a, d):
    return a+(d*(n-1))


def sum_counting(n):
    return (n*(n+1))/2


def sum_squares(n):
    return (n*(n+1)*((2*n)+1))/6


def sum_cubes(n):
    return ((n*n)*((n+1)*(n+1)))/4


def main():
    # part 1
    print("part 1: ")
    domain = {i for i in range(10)}
    co_domain = {i for i in range(9)}
    for func in [f0_same, f1_next, f2_prev, f3_double, f4_alt]:
        print(" function", func.__name__, get_function_type(func, domain, co_domain))
    # part 2
    print("part 2: ")
    X = {"a", "ab", "abc", "abcd"}
    Y = {"a", "bb", "ccc", "dddd"}
    print("X= {a, ab, abc, abcd}")
    print("Y= {a, bb, ccc, dddd}")
    print("xUy= ", set_union(X, Y))
    print("x intersection y= ", set_intersection(X, Y))
    print("X-Y= ", set_difference(X, Y))
    print("symmetric difference of X and Y= ", set_symmetric_difference(X, Y))
    print("XxY= ", set_cartesian_product(X, Y))
    print("P(X)= ", set_power_set(X))
    # part 3
    print("part 3: ")
    binary_numbers = ["0.111", "0.000", "0.101", "0.001", "0.011", "0.100"]
    print("New number is", generate_new_number(binary_numbers))
    # part 4
    print("part 4: ")
    a = 1
    r = 2
    n = 3
    d = 4
    print("a= ", a)
    print("r= ", r)
    print("n= ", n)
    print("d= ", d)
    print("geometric sum: ", sum_geometric_series(a, r, n))
    print("arithmetic sum: ", sum_arithmetic_series(n, a, d))
    print("counting sum: ", sum_counting(n))
    print("sum of the squares: ", sum_squares(n))
    print("sum of the cubes: ", sum_cubes(n))


if __name__ == "__main__":
    main()

