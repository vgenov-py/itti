# import requests as req
import json

# url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json"
# url_csv = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/ee750429-1e05-411a-b026-a57ea452a34a/download/municipio_comunidad_madrid.csv"
# res = req.get(url_csv)

# file = open("data.csv", "w")
# file.write(res.content.decode(errors="ignore"))
# file.close()

# data = res.content.decode()

# def get_data() -> dict:
#     file = open("data.json")
#     data = file.read()
#     data = json.loads(data)
#     file.close()
#     return data

def get_data() -> dict:
    file = open("data.json")
    data = json.load(file)
    file.close()
    return data

data = get_data()["data"] # <- list

def get_by_nie(ine:str) -> dict:
    for mun in data:
        if mun["municipio_codigo_ine"] == ine:
            return mun
        
# print(get_by_nie("280014"))

a = sum(map(lambda mun: mun["densidad_por_km2"] * mun["superficie_km2"], data))
# print(a)
# Función que permita encontrar municipio [dict] por código INE

# Función que permita encontrar un mun en base a cualquier clave con su respectivo valor

# get_by_key("municipio_codigo", "001")

def ley_benford(): # O(n) O(1) -> O(n*9) -> O(n)
    dic = {"1": 0, "2": 0, "3": 0, "4": 0,"5" : 0, "6": 0, "7": 0, "8": 0, "9": 0}
    [0.3,0.18,0.3] 
    for densidad in data: # 179 * 2 = 358
        densidad["densidad_por_km2"] = str(densidad["densidad_por_km2"])
        for num in dic: # 9 * 2 = 18
            if densidad["densidad_por_km2"][0] == num:
                dic[num] += 1
    for i in dic: # 9 * 3 = 27
        porcentaje = (dic[i] * 100) / len(data)
        print(f"Porcentaje de {i} : {porcentaje}%")

ley_benford()

def ley_benford_2(): # O(2 + 179*3 +9) -> O(n)
    result = {} # 1
    len_data = len(data) # 1
    for mun in data: # 179
        density = str(mun["densidad_por_km2"])[0] # 1
        try: # 1
            result[density] += 1/len_data # 1
        except KeyError:
            result[density] = 1/len_data # + 9

    def b(key_value:tuple) -> str:
        print(key_value)
        return key_value[0]
    print(result.items())
    print(dict(sorted(result.items(), key=b, reverse=False))) # 9 O(1)

ley_benford_2()

