def format_phone_number(phone: str) -> str:
    phone.strip()
    return f"{phone[0:4]} ({phone[4:6]}) {phone[6:9]}-{phone[9:11]}-{phone[11:13]}"


print(format_phone_number("+998971234567"))
# Output: +998 (97) 123-45-67
