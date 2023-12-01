import re
with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

digit_sum = 0
for line in lines:
    nums = re.findall(r'\d', line)
    cn = nums[0] + nums[-1]
    digit_sum += int(cn)

print(digit_sum)