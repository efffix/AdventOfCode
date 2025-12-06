import time
import math
MAX_NEIGHBORS = 4
INPUT = "input.txt"
start_time = time.perf_counter()



try:
    with open(INPUT, 'r') as file:
        full_lines = []
        total = 0
        for line in file:
            full_lines.append(line)

        num_matrix = list(zip(*full_lines))
        calc = 0
        sym = ''
        for t in num_matrix:
            num = ''.join(t[:-1]).strip()
            if num == '':
                total += calc
                calc = 0
                continue
            num = int(num)
            if t[-1].strip() != '':
                sym = t[-1]
            if calc == 0:
                calc = num
                continue
            if sym == '+':
                calc += num
            elif sym == '*':
                calc *= num

        print(total)

    end_time = time.perf_counter()
    print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
            
except Exception as e:
    print(f"An error occurred: {e}")