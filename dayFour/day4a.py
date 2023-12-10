def get_score(wining_numbs:list, played_numbs: list) -> int:
    scored_numbers = [winner for winner in played_numbs if winner in wining_numbs]
    if len(scored_numbers) == 0:
        return 0
    if len(scored_numbers) == 1:
        return 1
    else:
        score = 1
        for winner in range(len(scored_numbers)-1):
            score *= 2
        return score
def get_win_played_lists(clean_line:str) -> tuple:
    winning_num_list = [int(numb.strip()) for numb in clean_line.split("|")[0].split(':')[1].split(" ") if numb.strip() != ""]
    played_num_list = [int(numb.strip()) for numb in clean_line.split("|")[1].split(" ") if numb.strip() != ""]
    return(winning_num_list, played_num_list)
if __name__ == "__main__":
    with open("day4Data.txt") as f:
        lines = f.readlines()
    score_list = []
    for i in lines:
        win,play = get_win_played_lists(i)
        score_list.append(get_score(win,play))
    print(sum(score_list))