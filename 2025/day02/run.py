import time
start_time = time.perf_counter()
input_file = "input.txt"
total = 0

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 2
        
    if n > 2:
        factors.add(n)
        
    return factors

def get_numbers(start, end):
    numbers = set()
    factors = prime_factors(len(start))
    if len(factors) == 0:
        return set()
    for f in factors:
        step = int(len(start) / f)
        start_prefix = start[:step]
        end_prefix = end[:step]
        for i in range(int(start_prefix), int(end_prefix) + 1):
            num = str(i) * f
            if int(num) >= int(start) and int(num) <= int(end):
                numbers.add(int(num))
    return numbers


try:
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.split(',')
            for part in line:
                parts = part.split('-')
                if len(parts[0]) == len(parts[1]):
                    total += sum(get_numbers(parts[0], parts[1]))
                else:
                    if len(parts[1]) - len(parts[0]) > 1:
                        raise ValueError("Ranges differing by more than one digit length are not supported.")
                    mid = '9' * len(parts[0])
                    total += sum(get_numbers(parts[0], mid))
                    total += sum(get_numbers(str((int(mid) + 1)), parts[1]))
            
    print(total)
    end_time = time.perf_counter()
    print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
            
except Exception as e:
    print(f"An error occurred: {e}")


