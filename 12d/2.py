def calculate_painting_time(pattern: list) -> int: 
    sec = 0
    for i in range(len(pattern)-1):
        if pattern[i] != pattern[i+1]:
            sec += 1
    
    sec += 2 * len(pattern)

    return sec

pattern = ["Red", "Blue", "Red", "Blue", "Red"] 
print(calculate_painting_time(pattern)) 
# Output: 14
