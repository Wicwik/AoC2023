import re
with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

digit_map = {
    "one": "1", 
    "two": "2", 
    "three": "3", 
    "four": "4", 
    "five": "5", 
    "six": "6", 
    "seven": "7", 
    "eight": "8", 
    "nine": "9"
}

digit_sum = 0
new_lines = []
for line in lines:
    new_lines.append([])
    for k,v in digit_map.items():
        pos = [m.start() for m in re.finditer(k, line)]
        for p in pos:
            new_lines[-1].insert(p, (v,p))

        pos = [m.start() for m in re.finditer(v, line)]
        for p in pos:
            new_lines[-1].insert(p, (v,p))

for line in new_lines:
    line.sort(key = lambda x: x[1])
    digit_sum += int(line[0][0] + line[-1][0])
    print(line)

print(digit_sum)

