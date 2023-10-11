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

def decorador(fun):
    def inner():
        print("ESTO VIENE DE DECORADOR FUN")
        return fun()
    return inner

@decorador
def suma():
    return 1 + 1

r = suma()
r = suma()
r = suma()
r = suma()
r = suma()
r = suma()
r = suma()
print(r)


