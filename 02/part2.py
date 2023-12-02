with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

sum_mults = 0

for line in lines:
    counts = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    game_n = int(line.split(":")[0].split(" ")[1])
    game = line.split(":")[1]
    subsets = [i.strip() for i in game.split(";")]

    for s in subsets:
        dice = [i.strip() for i in s.split(",")]

        for d in dice:
            color = d.split(" ")[1]
            number = int(d.split(" ")[0])

            if number > counts[color]:
                counts[color] = number

    m = counts["red"] * counts["green"] * counts["blue"]
    sum_mults += m
    
print(sum_mults)

    