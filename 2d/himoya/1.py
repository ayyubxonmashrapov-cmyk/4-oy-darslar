def count_vowels_and_consonants(text: str) -> dict:
    unli_n = 0
    undosh_n = 0
    for i in text.lower():
        if i in ["a","e","u","i","o"]:
            unli_n += 1
        elif i in ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]:
            undosh_n += 1

    return f"{unli_n} {undosh_n}"


print(count_vowels_and_consonants("Salom Dunyo!"))



def find_top_seller(products: dict, sales: dict) -> str:
    return max(sales, key=lambda x: products[x] * sales[x])

print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10, "Banan": 5, "Uzum": 8}
))

def rearrange_by_frequency(nums: list[int]) -> list[int]:
    lst = [i for i in nums if nums.count(i)>1]
    lst.sort()

    st = set(nums)
    lst1 = [i for i in st if i not in lst]
    lst1.sort()

    lst.extend(lst1)
    return lst

print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))


import json
with open("student.json", "r") as file:
    students = json.load(file)

mx = max(students, key= lambda x: x["grade"])
mn = min(students, key= lambda x: x["grade"])
ortacha = sum([i["grade"] for i in students])/len(students)

print(f"eng yaxshi talaba {mx["name"]} - {mx["grade"]}\neng past baho {mn["name"]} - {mn["grade"]}\nortacha baho {ortacha}")