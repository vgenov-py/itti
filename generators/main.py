# Expresiones generadoras:

base_list = [1,2,3,4,5,6,7]
co_list = [num**2 for num in base_list] # [num**2 for num in base_list if num % 2 == 0] # [num**2 if num % 2 == 0 else num**3 for num in base_list]
# next(co_list)
gen_list = (num**2 for num in base_list)
print(next(gen_list))
# Funciones generadoras:

def n_2(data:list) -> list:
    result = []
    for num in data:
        result.append(num**2)
    return result

def gen_n_2(data:list):
    for num in data:
        yield num**2

# list_normal = n_2(base_list)
# list_gen = gen_n_2(base_list)
# print(list_normal)
# print(list(list_gen))
# print("-----------------------")
# print(list_normal)
# print(list(list_gen))
print(next(gen_n_2(base_list)))


def fibo(limit=15):
    result = [1,1]
    for _ in range(limit):
        result.append(result[-2] + result[-1])
    return result

def gen_fibo(limit=15):
    data = [1,1]
    for _ in range(limit):
        data.append(data[-2] + data[-1])
        yield data[-3]

# list_gen_fibo = list(gen_fibo())
a = gen_fibo()
print(next(a))