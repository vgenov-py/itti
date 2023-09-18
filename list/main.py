test = ["a", "b", "c", "d", "c"] # a,b,c,c,d

def count(iterable: list, value_to_search: any) -> int:
    counter = 0
    for value in iterable:
        if value == value_to_search:
            counter += 1
    return counter

# index:

def index(iterable: list, value_to_search: any) -> int:
    for v in enumerate(iterable):
        i = v[0]
        v = v[1]
        if v == value_to_search:
            return i

def index(iterable: list, value_to_search: any) -> int:
    for i, v in enumerate(iterable):
        if v == value_to_search:
            return i

# print(index(test, "b"))

repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]
print(set(repeated_numbers))