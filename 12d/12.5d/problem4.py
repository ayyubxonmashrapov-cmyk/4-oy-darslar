import json


def temperature_report():
    with open("data.json", "r") as file:
        data = json.load(file)

    dct = {}
    dct["averages"] = {}
    
    for i in data:
        dct['averages'][i] = sum(data[i]) / len(data[i])
    
    dct["hottest"] = max(dct["averages"], key=lambda x: dct["averages"][x])
    dct["coldest"] = min(dct["averages"], key=lambda x: dct["averages"][x])

    return dct


print(temperature_report())