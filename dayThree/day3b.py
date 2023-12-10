import re
import numpy as np
def pad_lines(lines_in_val: list) -> list:
    # pad lines
    lines_in = lines_in_val.copy()
    lines_in.insert(0,"".join(["." for i in range(len(lines_in[0]))]))
    lines_in.append(''.join(['.' for i in range(len(lines_in[0]))]))
    lines_in[-2] = lines_in[-2]+"."
    new_lines = [i.replace('\n', ".") for i in lines_in]
    new_lines = [ "." + l for l in new_lines]
    return new_lines
with open('day3AData.txt') as f:
    lines = f.readlines(0)
count_check = len(lines[0])
lines_clean = pad_lines(lines)
row_len = len(lines_clean[0])
lines_2 = "".join(lines_clean)
lines_2 = re.sub('\n', '.', lines_2)
num_locs = []
for i in re.finditer('\d{1,3}',lines_2):
    num_rang = []
    for num in range(i.start(), i.end()):
        num_rang.append(num)
    num_locs.append((num_rang,i.group(0)))
star_locs = []
for star_idx in re.finditer('\*',lines_2):
    idx = star_idx.start()
    idx_lst = [
        idx - row_len -1 , idx - row_len , idx - row_len + 1 ,
        idx -1 , idx , idx + 1 , idx + row_len-1 , idx + row_len , idx + row_len+1
    ]
    star_locs.append(idx_lst)
gears_list = []
for stars in star_locs:
    star_lst = []
    for numbers in num_locs:
        intersections = set(stars).intersection(set(numbers[0]))
        if len(intersections) !=0:
            star_lst.append(int(numbers[1]))
    if len(star_lst) > 1:
        gears_list.append(np.product(star_lst))
print(sum(gears_list))