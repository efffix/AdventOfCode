import time
MAX_NEIGHBORS = 4
INPUT = "input.txt"
start_time = time.perf_counter()


def count_neighbors(matrix, r, c):
    count = 0
    for row in [-1, 0, 1]:
        for col in [-1, 0, 1]:
            if row == 0 and col == 0:
                continue
            nr, nc = r + row, c + col
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                count += matrix[nr][nc]
    if count >= MAX_NEIGHBORS:
        return 0
    matrix[r][c] = 0
    return 1

def count_rolls(matrix):
    total = 0
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                continue
            total += count_neighbors(matrix, r, c)
    return total

try:
    with open(INPUT, 'r') as file:
        matrix = []
        for line in file:
            row = list(map(lambda x: 1 if x == "@" else 0, line.strip()))
            matrix.append(row)
        total = 0
        while True:
            count = count_rolls(matrix)
            total += count
            if count == 0:
                break
        print(total)

    end_time = time.perf_counter()
    print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
            
except Exception as e:
    print(f"An error occurred: {e}")