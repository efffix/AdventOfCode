import time
import math
MAX_NEIGHBORS = 4
INPUT = "input.txt"
start_time = time.perf_counter()



try:
    with open(INPUT, 'r') as file:
        full_lines = []
        num_matrix = []
        symbols = []
        total = 0
        for line in file:
            row = line.split()
            # row = list(map(lambda x: int(x), line.split()))
            num_matrix.append(row)
            full_lines.append(line)

        num_matrix = list(zip(*num_matrix))

        # print(num_matrix)

        s_id = len(num_matrix[0]) - 1 # symbol = col[s_id]
        y_line = 0
        
        for col in num_matrix:
            longest = len(max(col, key=len))
            numbers = ["" for x in range(longest)]
            for x in range(longest):
                for y in range(s_id):
                    numbers[x] += full_lines[y][y_line+x]
            y_line += longest + 1
            # print(numbers)

            calc = 0

            if col[s_id] == '+':
                # print('+')
                calc = sum(map(lambda x: int(x), numbers))
            if col[s_id] == '*':
                # print('*')
                calc = math.prod(map(lambda x: int(x), numbers))
            # i += 1
            # print(calc)
            total += calc
        # for col in zip(*num_matrix):
        #     print(col)
        #     calc = 0
        #     if symbols[i] == '+':
        #         calc = sum(col)
        #     if symbols[i] == '*':
        #         calc = math.prod(col)
        #     i += 1
        #     print(calc)
        #     total += calc

        # for i in range(len(symbols)):
        #     if symbols[i] == '+':
        #         total += sum(num_matrix[i])
        #     if symbols[i] == '*':
        #         total += math.prod(num_matrix[i])

        # for i in range(len(symbols)):
        #     if symbols[i] == '+':
        #         total += sum(idx) for idx in zip(*num_matrix)
        print(total)

    end_time = time.perf_counter()
    print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
            
except Exception as e:
    print(f"An error occurred: {e}")