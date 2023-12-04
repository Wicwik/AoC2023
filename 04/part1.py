with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

sum_wins = 0
for line in lines:
    s = line.split(":")[1].strip().split("|")
    win_nums = set(map(lambda x: int(x.strip()), filter(None, s[0].strip().split(" "))))
    my_nums = set(map(lambda x: int(x.strip()), filter(None, s[1].strip().split(" "))))

    n_wins = len(my_nums.intersection(win_nums))

    if n_wins > 0:
        sum_wins += pow(2,n_wins-1)

print(sum_wins)
