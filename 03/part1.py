with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]


sum_parts = 0
has_symbol = False


for i, line in enumerate(lines):
    if has_symbol:
        print(str_number)
        sum_parts += int(str_number)

    is_number = False
    has_symbol = False
    str_number = ''

    for j, char in enumerate(line):
        if char.isnumeric() and has_symbol:
            str_number += char
            continue

        if char.isnumeric():
            str_number += char

            if (i - 1) >= 0 and not lines[i-1][j].isnumeric() and lines[i-1][j] != '.':
                has_symbol = True
            
            elif (i + 1) < len(lines) and not lines[i+1][j].isnumeric() and lines[i+1][j] != '.':
                has_symbol = True

            elif (j - 1) >= 0 and not lines[i][j-1].isnumeric() and lines[i][j-1] != '.':
                has_symbol = True

            elif (j + 1) < len(lines[0]) and not lines[i][j+1].isnumeric() and lines[i][j+1] != '.':
                has_symbol = True

            elif (i - 1) >= 0 and (j - 1) >= 0 and not lines[i-1][j-1].isnumeric() and lines[i-1][j-1] != '.':
                has_symbol = True

            elif (i + 1) < len(lines) and (j + 1) < len(lines[0]) and not lines[i+1][j+1].isnumeric() and lines[i+1][j+1] != '.':
                has_symbol = True

            elif (i - 1) >= 0 and (j + 1) < len(lines[0]) and not lines[i-1][j+1].isnumeric() and lines[i-1][j+1] != '.':
                has_symbol = True

            elif (i + 1) < len(lines) and (j - 1) >= 0 and not lines[i+1][j-1].isnumeric() and lines[i+1][j-1] != '.':
                has_symbol = True

        else:
            if has_symbol:
                print(str_number)
                sum_parts += int(str_number)

            is_number = False
            has_symbol = False
            str_number = ''

            continue

print(sum_parts)