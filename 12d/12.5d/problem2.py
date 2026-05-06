def filter_orders(orders: list, target_status: str) -> list:
    result = []

    for order in orders:
        if order[3] == target_status and order[0].startswith("#") and order[2] > 0 and order[1]:
            result.append(order)

    return result

orders = [
    ("#101", "Aziz", 120, "new"),
    ("#102", "Laylo", 0, "new"),
    ("#103", "Jasur", 500, "processing"),
    ("A104", "Madina", 700, "new"),
    ("#105", "", 350, "delivered"),
    ("#106", "Kamola", 200, "delivered")
]

print(filter_orders(orders, "new"))
# Output: [("#101", "Aziz", 120, "new")]



print(filter_orders(orders, "delivered"))
# Output: [("#106", "Kamola", 200, "delivered")]
