import time

INPUT = "input.txt"

def validate(x1, y1, x2, y2, coords):
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    
    for i in range(len(coords)):
        j = i + 1
        if j >= len(coords):
            j = 0

        x_start, x_end = min(coords[i][0], coords[j][0]), max(coords[i][0], coords[j][0])
        y_start, y_end = min(coords[i][1], coords[j][1]), max(coords[i][1], coords[j][1])

        # line on y axis between y_start and y_end
        if x_start == x_end:
            # if line is within rectangle x bounds
            if x_start in range(min_x+1, max_x-1):
                # if line extends into rectangle y bounds
                if set(range(y_start, y_end+1)).intersection(set(range(min_y+1, max_y-1))):
                    return False
            
        # line on x axis
        if y_start == y_end:
            if y_start in range(min_y+1, max_y-1):
                if set(range(x_start, x_end+1)).intersection(set(range(min_x+1, max_x-1))):
                    return False
    return True

def find_limits(id, coords, min_x=0, max_x=100000, min_y=0, max_y=100000):
    (x, y) = coords[id]
    for i in range(len(coords)):
        j = i + 1
        if j >= len(coords):
            j = 0

        x_start, x_end = min(coords[i][0], coords[j][0]), max(coords[i][0], coords[j][0])
        y_start, y_end = min(coords[i][1], coords[j][1]), max(coords[i][1], coords[j][1])

        # line on y axis between y_start and y_end
        if x_start == x_end:
            if x_start == x:
                continue
            if x_start < x:
                if y in range(y_start, y_end):
                    min_x = max(min_x, x_start)
            else:
                if y in range(y_start, y_end):
                    max_x = min(max_x, x_start)
            
        # line on x axis
        if y_start == y_end:
            if y_start == y:
                continue
            if y_start < y:
                if x in range(x_start, x_end):
                    min_y = max(min_y, y_start)
            else:
                if x in range(x_start, x_end):
                    max_y = min(max_y, y_start)
    return [min_x, max_x, min_y, max_y]
    
    

try:
    start_time = time.perf_counter()
    
    with open(INPUT, 'r') as file:
        coords = [list(map(int, line.strip().split(','))) for line in file]
    
    limits = []
    min_x = min(coords, key=lambda item: item[0])[0]
    max_x = max(coords, key=lambda item: item[0])[0]
    min_y = min(coords, key=lambda item: item[1])[1]
    max_y = max(coords, key=lambda item: item[1])[1]
    for i in range(len(coords)):
        limits.append(find_limits(i, coords, min_x, max_x, min_y, max_y))   

    max_rectangle = 0
    for i in range(len(coords)):
        x1, y1 = coords[i]
        min_x, max_x, min_y, max_y = limits[i]
        for j in range(i+1, len(coords)):
            x2, y2 = coords[j]
            if x2 < min_x or x2 > max_x or y2 < min_y or y2 > max_y:
                continue

            min_x2, max_x2, min_y2, max_y2 = limits[j]
            if x1 < min_x2 or x1 > max_x2 or y1 < min_y2 or y1 > max_y2:
                continue

            rect_area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if rect_area > max_rectangle:
                if validate(x1, y1, x2, y2, coords):
                    max_rectangle = rect_area
                    #print(f"New largest: {max_rectangle} at ({x1},{y1}) to ({x2},{y2})")
    
    print(f"Largest rectangle: {max_rectangle}")
    print(f"Execution time: {(time.perf_counter() - start_time) * 1000:.2f} ms")
    
except Exception as e:
    print(f"Error: {e}")
    raise