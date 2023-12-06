def valid_game(inline: str) -> bool:
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
    bool_list = []
    for hand in my_hands_list:
        bool_list.append(all([hand['red'] <= 12,hand['green'] <= 13,hand['blue'] <= 14  ]))
    results = all(bool_list)
    return results

with open("dayTwoAData.txt") as f:
    lines = f.readlines()

valide_game_list =[]
for n,line in enumerate(lines):
    if valid_game(line):
        valide_game_list.append(n+1)

print(sum(valide_game_list))