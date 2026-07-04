def simple_lcg(seed, iterations=5):
    # Constants traditionally used in older systems (like glibc)
    a = 1103515245
    c = 12345
    m = 8
    
    current_value = seed
    results = []
    
    for _ in range(iterations):
        # The core LCG formula
        current_value = (a * current_value + c) % m
        results.append(current_value)
        
    return results
print(simple_lcg(8,5))