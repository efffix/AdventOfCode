input_file = "input.txt"
allowed_directions = ['R', 'L']
password = 0
dial = 50

try:
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            if direction not in allowed_directions:
                raise ValueError('Direction must be R or L')
            distance = int(line[1:])
            #password += distance // 100
            #distance %= 100
        
            if direction == 'R':
                dial += distance
                password += dial // 100
                dial %= 100
            if direction == 'L':
                if dial == 0:
                    password -= 1
                dial -= distance
                
                if dial % 100 == 0:
                    # Falls on 0. +1
                    password += 1
                    # if < 0, rotated before falling on 0
                    password += (dial // -100)
                    dial = 0
                elif dial < 0:
                    #crossed 0 at least once
                    password += 1
                    # if < -100, crossed 0 a few more times
                    password += dial // -100
                    dial %= 100
    print(password)
            
except Exception as e:
    print(f"An error occurred: {e}")