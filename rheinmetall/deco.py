# import datetime as dt

# def suma(a,b):
#     return a + b


# def decorador(fun,*cualquiercosa):
#     with open("funcs.log", "a", encoding="utf-8") as file:
#         result = fun(*cualquiercosa)
#         file.write(f"{dt.datetime.now()}|{fun.__name__}\n")
#     return result

# r = decorador(suma,7,32)
# print(r)

# decorador(print, "para imprimir algo")
# def resta(a,b):
#     return a-b
# print(decorador(resta, 22,2))
# def elevar(num):
#     return num ** 2

# list(map(elevar(32), (1,2,3,4)))

"Decorador de verdad:"

def decorador(function_to_decorate):
    def inner(*args):
        return function_to_decorate(*args)
    return inner

import datetime as dt

def decorador(f):
    name = f.__name__
    def inner(*args):
        with open("funcs.log", "a", encoding="utf-8") as file:
            file.write(f"{dt.datetime.now()}|{name}|Vito\n")
        return f(*args)
    return inner


@decorador
def suma(a:int,b:int):
    return a + b

@decorador
def resta(a:int, b:int):
    return a - b 

print("A")
if __name__ == "__main__":
    print(__name__)
    print("Algo en el medio")
    result = suma(3,2)
    result = resta(3,2)
    result = resta(3,2)
    result = resta(3,2)
    result = resta(3,2)
    result = resta(3,2)
    print(result)