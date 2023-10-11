import requests as req

def get_stock():

    user_symbol = input("Symbol: ")
    try:
        url = f"https://api.twelvedata.com/time_series?apikey=74ba75970dee40e087c8f3f4ff52ed6b&symbol={user_symbol}&interval=1day&exchange=NYSE&type=stock&start_date=2023-02-23&end_date=2023-02-26&format=json"

        res = req.get(url).json()

        values = res["values"]

        for v in values:
            print(v + "s")
        
        return v
    
    except KeyError as e:
        print("Símbolo no encontrado")

    except TypeError as e:
        print("Escribí código malo")


print(get_stock())