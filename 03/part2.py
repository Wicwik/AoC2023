with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]


sum_parts = 0
has_symbol = False
symbol_pos = None

gear_numbers = {}
gears = {}

for i, line in enumerate(lines):
    if has_symbol:
        print(str_number)
        sum_parts += int(str_number)

        if not gears.get(symbol_pos):
            gears[symbol_pos] = [int(str_number)]
        else:
            gears[symbol_pos].append(int(str_number))

    is_number = False
    has_symbol = False
    str_number = ''
    symbol_pos = None

    for j, char in enumerate(line):
        if char.isnumeric() and has_symbol:
            str_number += char
            continue

        if char.isnumeric():
            str_number += char

            if (i - 1) >= 0 and not lines[i-1][j].isnumeric() and lines[i-1][j] != '.':
                if lines[i-1][j] == '*':
                    if not gear_numbers.get((i-1, j)):
                        gear_numbers[(i-1, j)] = 1
                    else:
                        gear_numbers[(i-1, j)] += 1
                
                    has_symbol = True
                    symbol_pos = (i-1, j)
            
            elif (i + 1) < len(lines) and not lines[i+1][j].isnumeric() and lines[i+1][j] != '.':
                if lines[i+1][j] == '*':
                    if not gear_numbers.get((i+1, j)):
                        gear_numbers[(i+1, j)] = 1
                    else:
                        gear_numbers[(i+1, j)] += 1
            
                    has_symbol = True
                    symbol_pos = (i+1, j)

            elif (j - 1) >= 0 and not lines[i][j-1].isnumeric() and lines[i][j-1] != '.':
                if lines[i][j-1] == '*':
                    if not gear_numbers.get((i, j-1)):
                        gear_numbers[(i, j-1)] = 1
                    else:
                        gear_numbers[(i, j-1)] += 1
                
                    has_symbol = True
                    symbol_pos = (i, j-1)

            elif (j + 1) < len(lines[0]) and not lines[i][j+1].isnumeric() and lines[i][j+1] != '.':
                if lines[i][j+1] == '*':
                    if not gear_numbers.get((i, j+1)):
                        gear_numbers[(i, j+1)] = 1
                    else:
                        gear_numbers[(i, j+1)] += 1

                    has_symbol = True
                    symbol_pos = (i, j+1)

            elif (i - 1) >= 0 and (j - 1) >= 0 and not lines[i-1][j-1].isnumeric() and lines[i-1][j-1] != '.':
                if lines[i-1][j-1] == '*':
                    if not gear_numbers.get((i-1, j-1)):
                        gear_numbers[(i-1, j-1)] = 1
                    else:
                        gear_numbers[(i-1, j-1)] += 1
                
                    has_symbol = True
                    symbol_pos = (i-1, j-1)

            elif (i + 1) < len(lines) and (j + 1) < len(lines[0]) and not lines[i+1][j+1].isnumeric() and lines[i+1][j+1] != '.':
                if lines[i+1][j+1] == '*':
                    if not gear_numbers.get((i+1, j+1)):
                        gear_numbers[(i+1, j+1)] = 1
                    else:
                        gear_numbers[(i+1, j+1)] += 1

                    has_symbol = True
                    symbol_pos = (i+1, j+1)

            elif (i - 1) >= 0 and (j + 1) < len(lines[0]) and not lines[i-1][j+1].isnumeric() and lines[i-1][j+1] != '.':
                if lines[i-1][j+1] == '*':
                    if not gear_numbers.get((i-1, j+1)):
                        gear_numbers[(i-1, j+1)] = 1
                    else:
                        gear_numbers[(i-1, j+1)] += 1

                    has_symbol = True
                    symbol_pos = (i-1, j+1)

            elif (i + 1) < len(lines) and (j - 1) >= 0 and not lines[i+1][j-1].isnumeric() and lines[i+1][j-1] != '.':
                if lines[i+1][j-1] == '*':
                    if not gear_numbers.get((i+1, j-1)):
                        gear_numbers[(i+1, j-1)] = 1
                    else:
                        gear_numbers[(i+1, j-1)] += 1

                    has_symbol = True
                    symbol_pos = (i+1, j-1)

        else:
            if has_symbol:
                print(str_number)
                sum_parts += int(str_number)

                if not gears.get(symbol_pos):
                    gears[symbol_pos] = [int(str_number)]
                else:
                    gears[symbol_pos].append(int(str_number))


            is_number = False
            has_symbol = False
            str_number = ''
            symbol_pos = None

            continue

sum_parts = 0


for pos, g in gears.items():
    if len(g) == 2:
        sum_parts += g[0]*g[1]

print(sum_parts, gear_numbers, gears)