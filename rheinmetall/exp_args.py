base_list = [1,2,3,4]

def mean(data:list=[1,2,3,4]) -> float:
    result = 0
    for num in data:
        result += num
    return result/len(data)

def mean(*values:int) -> float:
    result = 0
    print(type(values))
    print(values)
    for num in values:
        result += num
    return result/len(values)

# print(mean(*base_list)) # -> mean(1,2,3,4)

def nums_square(data:list) -> list:
    result = []
    for num in data:
        result.append(num**2)
    return result

# print(nums_square(base_list))

def nums_square(*args:list) -> list:
    result = []
    for num in args:
        result.append(num**2)
    return result

# print(nums_square(1,2,3,4))
