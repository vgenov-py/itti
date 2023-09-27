import requests as req
import json

url = "https://api.twelvedata.com/time_series?apikey=74ba75970dee40e087c8f3f4ff52ed6b&symbol=LMT&interval=1day&exchange=NYSE&type=stock&start_date=2021-02-23 20:27:00&end_date=2023-09-26 20:27:00&format=json"



'''
Alemanes:
 "2019-09-11": {
            "1. open": "115.1500",
            "2. high": "117.2000",
            "3. low": "115.1500",
            "4. close": "116.5000",
            "5. volume": "119903"
},
Americanos:
        {
            "datetime": "2023-09-26",
            "open": "410.63000",
            "high": "411.26999",
            "low": "407.87360",
            "close": "409.80991",
            "volume": "546037"

}
result:
{
    {
    "RHM": [float...], ASC
    "LMT": [float...] ASC
    }
}
'''
data = {"RHM":[], "LMT":[]}
with open("LMT.json") as file:
    lmt = json.load(file) # load loads dump dumps utf-8
    "ORDENAR VALUES:"
    "sorted - sort"
    def return_datetime(stock):
        return stock["datetime"]
    values = sorted(lmt["values"], key=return_datetime)
    values = [float(stock["close"]) for stock in values]
    data["LMT"] = values

with open("RHM.json") as file:
    rhm = json.load(file)
    values = rhm["Time Series (Daily)"]
    def return_datetime(stock:tuple) -> str:
        return stock[0]
    values = sorted(list(values.items()), key=return_datetime)
    values = [float(stock[1]["4. close"]) for stock in values if stock[0] >= "2021-02-24"]
    data["RHM"] = values

file = open("data.json", "w")
json.dump(data, file)
file.close()


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

"1. Calculas las medias de las acciones desde el 24/02/2021 - 23/02/2022 y desdel el 24/02/2022 - 26/09/2023"









