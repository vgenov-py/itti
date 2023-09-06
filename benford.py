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
print(a)
# Función que permita encontrar municipio [dict] por código INE

# Función que permita encontrar un mun en base a cualquier clave con su respectivo valor

# get_by_key("municipio_codigo", "001")