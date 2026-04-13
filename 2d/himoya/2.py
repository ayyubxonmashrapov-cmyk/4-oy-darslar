def find_most_abundant(products: dict) -> str|None:
    return max(products, key=lambda x : products[x])

products = {"olma": 17, "banan": 3, "sut": 10}
print(find_most_abundant(products))



def find_product_by_id(products: list, product_id: str):
    for i in products:
        if i[0] == product_id:
            return i 

products = [("ID123", "Olma", 10), ("ID101", "Banan", 5), ("ID150", "Anor", 8)]
print(find_product_by_id(products, "ID101"))


def format_date(date_str: str) -> str:
    stg = date_str.split()
    dct = {    
        "yanvar": "01", 
        "fevral": "02", 
        "mart": "03", 
        "aprel": "04",
        "may": "05", 
        "iyun": "06", 
        "iyul": "07", 
        "avgust": "08",
        "sentyabr": "09", 
        "oktyabr": "10", 
        "noyabr": "11", 
        "dekabr": "12"
    }
    return f"{stg[0]}.{dct[stg[1]]}.{stg[2]}"

print(format_date("24 mart 2025"))



import json

with open("book.json", "r") as file:
    books = json.load(file)

print(*[i["title"] for i in books])
print(max(books, key=lambda x: x["copies"])["title"])


