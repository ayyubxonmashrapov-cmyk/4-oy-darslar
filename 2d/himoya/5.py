def sum_numbers_in_text(text: str) -> int:
    words = text.split()
    n = 0
    for i in words:
        if i.isdigit() or i[1:].isdigit():
            n += int(i)
    return n        

print(sum_numbers_in_text("10 olma 20 -5 6"))  
# Output: 31

def convert_to_seconds(time_str: str) -> int:
    hour, minute, second = time_str.split(":")
    hour *= 3600
    minute *= 60
    return hour + minute + second 


