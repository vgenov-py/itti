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
# print(list(set(repeated_numbers)))
def unique_list(iterable: list) -> list:
    result = []
    for v in iterable: # O(n)
        if v not in result: # O(n[result])  
            result.append(v) # + 1
    return result 

# print(unique_list(repeated_numbers))

def unique_list_2(iterable: list) -> list:
    result = []
    last_n = None
    iterable = sorted(iterable) # O(n)
    for v in iterable: # O(n)
        if v != last_n:
            result.append(v)
        last_n = v
    return result # O(n*2)

# print(unique_list_2(repeated_numbers))

def unique_list_3(iterable: list) -> list:
    result = []
    for v in iterable: # O(n**2)
        if iterable.count(v) == 1:
            result.append(v)
    return result

'''
n = 100
for v in iterable: O(n) Operations: 100
    algo
    for v in iterable: O(n**2) Opearations: 10000
        algo
'''

'''
n = 100 O(n*2)
for v in iterable: O(n) Operations: 100
    algo
for v in iterable: O(n) Opearations: 100
    algo

def a()
    for num in a 
        for num in a
            ()

'''

# 5.

unique_nums = unique_list(repeated_numbers)
# print(unique_nums)
result = []

for num in unique_nums:
    result.append(num**2)

# [_ for _ in _]
a = [num**2 for num in unique_nums]

a = [num**2 for num in unique_nums if num % 2 == 0]
# print(a == result)
# print(a)

# b = 3
# if b  % 2 == 0:
#     print("Es par")

# # _ if _ else _
# is_even = "Es par" if b  % 2 == 0 else "Es impar"
# print(is_even)

# ------EXPLICACIÓN GENERATOR:
import time
unique_nums = range(20349000)
# start = time.perf_counter()
# result = []
# b = [num ** 2 if num % 2 == 0 else num ** 3 for num in unique_nums] # O(n)
# for num in b: # O(n)
#     result.append(num ** 2)
# del(b)
# end = time.perf_counter()
# # print("Comprehension list: ",end-start)
# # print(dir(b))

# start = time.perf_counter()
# result = []
# pow_2_nums_ge = (num ** 2 if num % 2 == 0 else num ** 3 for num in unique_nums) # O() NADA
# for num in pow_2_nums_ge: # O(n)
#     result.append(num ** 2)

# end = time.perf_counter()

# start = time.perf_counter()
# mean = sum(unique_nums)/len(unique_nums)
# print(mean)
# end = time.perf_counter()
# print(end-start)

# print("-----------------")
# from numpy import mean

# start = time.perf_counter()
# a = mean(unique_nums)
# print(a)
# end = time.perf_counter()
# print(end-start)
'''
7. Encontrar el valor máximo de la lista y cambiarlo por 1000
'''

unique_nums = unique_list(repeated_numbers)
# unique_nums = list(range(20349000))
start = time.perf_counter()
unique_nums[unique_nums.index(max(unique_nums))] = 1000
end = time.perf_counter()
# print(end-start)
# print(".-............")
def change_max_1000():
    highest_num_recorded = 0
    max_i = 0
    for i, num in enumerate(unique_nums):
        if num > highest_num_recorded:
            highest_num_recorded = num
            max_i = i
    unique_nums[max_i] = 1000
    return unique_nums
start = time.perf_counter()
change_max_1000()
end = time.perf_counter()
# print(end-start)
# print(unique_nums)
# print(sum(unique_nums[4:10]))
result = 0
for i, num in enumerate(unique_nums):
    if i >= 4 and i < 10:
        result += num
# print(result)

def fibonacci(limit=15):
    lista_fibo = [1, 1]
    for num in lista_fibo: # O(n)
        sum = lista_fibo[-1] + lista_fibo[-2]
        lista_fibo.append(sum)
        if len(lista_fibo) == limit:
            return lista_fibo
            break
print(fibonacci(6))