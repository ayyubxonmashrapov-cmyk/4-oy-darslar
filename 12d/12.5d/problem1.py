def merge_user_logs(log1: dict, log2: dict) -> str:
    for user in log1:
        if user in log2:
            log2[user] += log1[user]
        else:
            log2[user] = log1[user]
    
    return log2

print(merge_user_logs({"aziz": 5, "laylo": 3, "jasur": 2},{"jasur": 4, "aziz": 1, "madina": 7}))

