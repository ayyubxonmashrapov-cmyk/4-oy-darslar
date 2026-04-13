
def format_phone_number(phone: str) -> str:
    a = phone[0:4]
    b = phone[4:6]
    c = phone[6:9]
    d = phone[9:11]
    e = phone[11:13]
    return f"{a} ({b}) {c}-{d}-{e}"

print(format_phone_number("+998971234567"))



def calculate_difference_percentage(user1: set, user2: set) -> float:
    st = user1.difference(user2)
    st1 = user1.intersection(user2)
    return len(st) / len(st1) * 100

user1 = {"Titanic", "Avatar", "Inception", "Matrix"}
user2 = {"Avatar", "Inception", "IronMan"}

print(calculate_difference_percentage(user1, user2))


