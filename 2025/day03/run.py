import time
start_time = time.perf_counter()

input_file = "input.txt"
total = 0
BATTERY_COUNT = 12

def highest_digit(battery_number, line):
    # If rest of line length equals remaining batteries, take all digits
    if (BATTERY_COUNT - battery_number + 1) == len(line):
        return int(line), battery_number
    # If, otherwise -0 breaks thing for last battery
    line = line[:-(BATTERY_COUNT - battery_number)] if (BATTERY_COUNT - battery_number) != 0 else line
    for i in range(9,0,-1):
        index = line.find(str(i))
        if index != -1:
            return i, index

try:
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            last_battery_position = 0
            battery_strength = ""
            for i in range(1, BATTERY_COUNT + 1):
                digit, index = highest_digit(i, line[last_battery_position:])
                last_battery_position += index + 1
                battery_strength += str(digit)
                if len(battery_strength) == BATTERY_COUNT:
                    break
            total += int(battery_strength)                   
            
    print(total)
    end_time = time.perf_counter()
    print(f"Execution time: {(end_time - start_time) * 1000} milliseconds")
            
except Exception as e:
    print(f"An error occurred: {e}")