with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

r = 12
g = 13
b = 14

count_games = 0

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

    if counts["red"] <= r and counts["green"] <= g and counts["blue"] <= b:
        count_games += game_n


print(count_games)

    
