with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

cards = {}

for line in lines:
    n_line = int(line.split(":")[0].split(" ")[-1])
    cards[n_line] = 1

for line in lines:
    n_line = int(line.split(":")[0].split(" ")[-1])
    s = line.split(":")[1].strip().split("|")
    win_nums = set(map(lambda x: int(x.strip()), filter(None, s[0].strip().split(" "))))
    my_nums = set(map(lambda x: int(x.strip()), filter(None, s[1].strip().split(" "))))

    n_wins = len(my_nums.intersection(win_nums))

    for i in range(1, n_wins+1):
        cards[n_line + i] += cards[n_line ]*1

cards_sum = 0
for k,v in cards.items():
    cards_sum += v

print(cards_sum)
