# import requests as req
import json

url = "https://api.twelvedata.com/time_series?apikey=74ba75970dee40e087c8f3f4ff52ed6b&symbol=LMT&interval=1day&exchange=NYSE&type=stock&start_date=2021-02-23 20:27:00&end_date=2023-09-26 20:27:00&format=json"

data = {"RHM":[], "LMT":[]}
with open("LMT.json") as file:
    lmt = json.load(file) # load loads dump dumps utf-8
    "ORDENAR VALUES:"
    "sorted - sort"
    def return_datetime(stock):
        return stock["datetime"]
    values = sorted(lmt["values"], key=return_datetime)
    values = [{f"{stock['datetime']}":float(stock["close"])} for stock in values]
    data["LMT"] = values

with open("RHM.json") as file:
    rhm = json.load(file)
    values = rhm["Time Series (Daily)"]
    def return_datetime(stock:tuple) -> str:
        return stock[0]
    values = sorted(values.items(), key=return_datetime)
    values = [{f"{stock[0]}":float(stock[1]["4. close"])} for stock in values if stock[0] >= "2021-02-24"]
    data["RHM"] = values

# file = open("data.json", "w")
# json.dump(data, file)
# file.close()


'''
Análisis Rheinmetall:
'''

'''
1. Calcular media 
2. Calcular cuasivarianza
3. Calcular T de Student
4. Calcular grados de libertad
5. Calcular R de Pearson
'''

"1. Calculas las medias de las acciones desde el [24/02/2021 - 23/02/2022] y desdel el [24/02/2022 - 26/09/2023] - Rheinmetall"
"Crear una función que acepte una fecha de incio y una fecha final"



with open("data.json") as file:
    data = json.load(file)
    data = data["RHM"]


def mean(data:list, s:str, e:str) -> float:
    result = 0
    len_data = 0
    for value in data:
        date, stock = list(value.items())[0] # 1º value: ("2021-02-24", 84.92)
        if date >= s and date <= e:
            result += stock
            len_data += 1
    return result/len_data

'''
1. Al menos un parámetro
2. return asociado
3. NO se pueden asignar valores
'''

values = [1,2,3,4]

# 1
def b_map(data:list) -> list:
    result = []
    for num in data:
        result.append(num)
    return result

def return_value(value):
    return value

# 2
# print(list(map(return_value,values))) # 1. for 2. append 3. return

# 3
# print(list(map(lambda value: value,values))) # 1. for 2. append 3. return 4. Ejecucción la función

# 4

def my_map(fun, data:list) -> list:
    result = []
    for value in data:
        result.append(fun(value))
    return result

c = my_map(lambda value: value,values)

# 5
def my_map_gen(fun, data:list):
    for value in data:
        yield fun(value)

d = my_map_gen(lambda value:value, values)


values = [1,2,3,4]
values = list(map(lambda value:value**2, values))

# result = list(filter(lambda value: value % 2 == 0,values))
# users = [{}]

# def divide_users(users:list, group:int) -> list:
#     result = []
#     for user in users:
#         if user["group"] == group:
#             result.append(user)
#     return result

# list(filter(lambda user:user["group"] == 1, users)) # 1. for, 2. append, 3. if keyword, 4. return

# print(result)


def mean(data:list, s:str, e:str) -> float:
    result = 0
    len_data = 0
    for value in data:
        date, stock = list(value.items())[0] # 1º value: ("2021-02-24", 84.92)
        if date >= s and date <= e:
            result += stock
            len_data += 1
    return result/len_data

mean_basic = mean(data, "2022-02-24", "2023-09-26")
# print(mean_basic)

# lista con los precios dentro del intervalo
# sum(lista)/len(lista)

'''
stock_dict = {
            "2021-02-24": 84.92
}

list(stock_dict.keys())[0]
'''
s,e = "2021-02-24", "2022-02-23"
# stock_price_bw = filter(lambda stock_dict: list(stock_dict.keys())[0] >= s and list(stock_dict.keys())[0] <= e, data) # 1. for
# stock_price_bw = list(map(lambda stock_dict: list(stock_dict.values())[0], stock_price_bf))
# print(sum(stock_price_bw)/len(stock_price_bw))


def stock_price_by_interval(data:list, s:str, e:str) -> list:

    def return_stock_price_if_date(stock_dict:dict) -> float:
        date, stock = list(stock_dict.items())[0]
        if date >= s and date <= e:
            return stock

    return [value for value in map(return_stock_price_if_date,data) if value]

stock_before_war = stock_price_by_interval(data, s,e)
stock_after_war = stock_price_by_interval(data, "2022-02-24","2023-09-26")

mean_bw = sum(stock_before_war)/len(stock_before_war)

mean_aw = sum(stock_after_war)/len(stock_after_war)


# print(mean_aw)

'''
symbol,after_conflict,mean\n
RHM,0,80\n
RHM,1,211

2. Calcular varianza
Y == MEDIA
Σ₁
# 90, 90, 90, 90, 90
Σ(y₁-Ȳ)² / n - 1

1. Por cada puntuación restar la media y elevar al cuadrado
2. De ese resultado, obtener el sumatorio
3. Dividir por n - 1
'''

def variance(data:list) -> float:
    result = 0
    mean = sum(data)/len(data)
    for value in data:
        result += (value - mean)**2
    result = result/(len(data) - 1)
    return result
'''
for i, algo in enumerate(algos):

'''
# print(variance(stock_before_war)) # map - filter - reduce

# map
n = len(stock_before_war)
def map_variance(data:list, mean: float) -> float:
    n = len(data)
    return sum(map(lambda value: ((value-mean)**2)/(n-1), data))

v_bw = map_variance(stock_before_war, mean_bw)
v_aw = map_variance(stock_after_war, mean_aw)
# print(v_aw)

# s,e = "2021-02-24", "2022-02-23"


dates_stocks = map(lambda dict_stock: tuple(dict_stock.items())[0],data)
dates_stocks_bw = filter(lambda stock_price: stock_price[0] >= s and stock_price[0] <= e , dates_stocks)
# print(tuple(map(lambda date_stock: date_stock[1],dates_stocks_bw)))
# print(sum(map(lambda value: ((value[1]-mean_bw)**2)/(n-1), dates_stocks_bw)))

# print(sum(map(lambda value: ((value[1]-mean_bw)**2)/(n-1), filter(lambda stock_price: stock_price[0] >= s and stock_price[0] <= e , map(lambda dict_stock: tuple(dict_stock.items())[0],data)))))

# Grados de libertad:

def df(s1,s2,n1,n2) -> float:
    den = (s1/n1+s2/n2)**2
    nom = (((s1/n1)**2)/(n1-1)) + (((s2/n2)**2)/(n2-1))
    return den/nom

print("cuasivarianza bw: ", v_bw)
print("cuasivarianza aw: ", v_bw)
df_rheinmetall = df(v_aw, v_bw, len(stock_after_war), len(stock_before_war))
print("Grados de libertad: ",df_rheinmetall)

# T de Student:

def t_student(mean1, mean2, s1,s2,n1,n2) -> float:
    den = mean1 - mean2
    nom = ((s1/n1)+(s2/n2))**0.5
    return den/nom

t_value = t_student(mean_aw, mean_bw, v_aw, v_bw, len(stock_after_war), len(stock_before_war))
print("T Student: ",t_value)

headers = "symbol,n,mean,variance,t_student,d.f."
row_1 = f"RHM_1,{len(stock_before_war)},{mean_bw},{v_bw},{t_value},{df_rheinmetall}"
row_2 = f"RHM_2,{len(stock_after_war)},{mean_aw},{v_aw},,"
to_write = [headers,row_1,row_2]

print(to_write)

def export_txt(file_name:str, content:list):
    file = open(file_name, "w", encoding="utf-8")
    file.writelines(f"{row}\n" for row in content)
    file.close()

export_txt("result.txt", to_write)