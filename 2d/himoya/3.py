def merge_user_logs(log1: dict, log2: dict) -> str:
    for i in log1.keys():
        if i in log2:
            log2[i] += log1[i]
        else:
            log2[i] = log1[i]    
    return log2

print(merge_user_logs(
    {"aziz": 5, "laylo": 3, "jasur": 2},
    {"jasur": 4, "aziz": 1, "madina": 7}
))



def filter_orders(orders: list, target_status: str) -> list:
    result = []
    for i in orders:
        if i[0][0] == "#" and i[2]>0 and i[1] != "" and i[3] == target_status:
            result.append(i)
    return result        

orders = [
    ("#101", "Aziz", 120, "new"),
    ("#102", "Laylo", 0, "new"),
    ("#103", "Jasur", 500, "processing"),
    ("A104", "Madina", 700, "new"),
    ("#105", "", 350, "delivered"),
    ("#106", "Kamola", 200, "delivered")
]
print(filter_orders(orders, "delivered"))



def analyze_sentence(sentence: str) -> dict:
    words = sentence.split()
    endsimvol = True if sentence[-1] == "." else False
    words_n = len(words)
    longest = max(words, key=lambda x: len(x))
    dct= {
        "words": words_n,
        "longest": longest,
        "ends_with_dot": endsimvol 
    }
    return dct


print(analyze_sentence("Python dasturi juda qulay va dasturchilarga yoqadi."))


import json
def temperature_report(temps: list[dict])->dict:
    dct = {
        "averages": {},
        "hottest": 0,
        "coldest": 0,

    }
    for i in temps.keys():
        dct["averages"].update({i: sum(temps[i])/len(temps[i])})
    
    dct["hottest"] = max(dct["averages"].items(), key= lambda x: x[1])[0]
    dct["coldest"] = min(dct["averages"].items(), key= lambda x: x[1])[0]

    return dct

with open("/Users/probox/ayyub/najotTAlim/4.oy/2d/himoya/temps.json", "r") as file:
    temps = json.load(file)

print(temperature_report(temps))    