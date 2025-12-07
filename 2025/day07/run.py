import time
import math
MAX_NEIGHBORS = 4
INPUT = "input.txt"
start_time = time.perf_counter()



try:
    with open(INPUT, 'r') as file:
        matrix = []
        total = 0
        line = file.readline()
        matrix.append(list(map(lambda x: 1 if x == 'S' else 0, line)))
        line_number = 1
        for line in file:
            matrix.append([0] * len(matrix[0]))
            i = 0
            for c in line:
                if matrix[line_number-1][i] > 0:
                    if c == '^':
                        matrix[line_number][i-1] += matrix[line_number-1][i]
                        matrix[line_number][i+1] += matrix[line_number-1][i]
                    else:
                        matrix[line_number][i] += matrix[line_number-1][i]
                i += 1
            line_number += 1
        print(sum(matrix[line_number-1]))
        
    end_time = time.perf_counter()
    print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
            
except Exception as e:
    print(f"An error occurred: {e}")