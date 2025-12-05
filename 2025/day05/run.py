import time
MAX_NEIGHBORS = 4
INPUT = "input.txt"
start_time = time.perf_counter()

def combine_sorted_ranges(ranges):
    if not ranges:
        return []
    combined = [ranges[0]]
    for current in ranges[1:]:
        last = combined[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            combined.append(current)
    return combined

# def check_freshness(fresh, ingredient):
#     for fr in fresh:
#         if fr[0] <= ingredient <= fr[1]:
#             return 1
#     return 0

try:
    with open(INPUT, 'r') as file:
        fresh = []
        ingredients = []
        while True:
            line = file.readline().strip()
            if line == "":
                break
            fresh_range = line.split('-')
            fresh.append([int(fresh_range[0]), int(fresh_range[1])])
        fresh = sorted(fresh, key=lambda x: (int(x[0]), int(x[1])))
        # for line in file:
        #     ingredients.append(int(line.strip()))
        # total = sum(map(lambda x: check_freshness(fresh, x), ingredients))
        fresh = combine_sorted_ranges(fresh)
        print(sum(map(lambda x: x[1] - x[0] + 1, fresh)))

    end_time = time.perf_counter()
    print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
            
except Exception as e:
    print(f"An error occurred: {e}")