import numpy as np
def game_power(inline: str) -> bool:
    game = inline.split(":")[1]
    hands = game.split(";")
    my_hands_list = []
    for draw in hands:
        picks = draw.split(",")
        hand_dict = {
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }
        for i in picks:
            val = i.strip()
            hand_dict[val.split(' ')[1]] = int(val.split(' ')[0])
        my_hands_list.append(hand_dict)
    maxvals = {
    "redmax" : 0,
    "greenmax" : 0,
    "bluemax" : 0
    }
    for i in my_hands_list:
        if i['red'] > maxvals["redmax"]:
            maxvals["redmax"] = i['red']
        if i['green'] > maxvals["greenmax"]:
            maxvals["greenmax"] = i['green']
        if i['blue'] > maxvals['bluemax']:
            maxvals['bluemax'] = i['blue']
    power = np.product(list(maxvals.values()))
    return power

with open(r"dayTwoAData.txt") as f:
    lines = f.readlines()

power_list = []
for line in lines:
    power_list.append(game_power(line))
print(sum(power_list))