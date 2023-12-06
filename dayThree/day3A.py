import re

def pad_lines(lines: list) -> list:
    # pad lines
    lines.insert(0,"".join(["." for i in range(len(lines[0]))]))
    lines.append(''.join(['.' for i in range(len(lines[0]))]))
    lines[-2] = lines[-2]+"."
    new_lines = [i.replace('\n', ".") for i in lines]
    new_lines = [ "." + l for l in new_lines]
    return new_lines

def get_unique_chars(lines: list) -> set:
    chars = "".join(lines)
    vals = re.sub('\d{1,100}','.',chars)
    vals =  re.sub("\n", '.', vals)
    vals = vals.replace('.','')
    vals = set(vals)
    return vals

def include_part(intuple: tuple, file_lines: list, special_chars: list) -> bool:
    upper_range = file_lines[intuple[0]-1][intuple[1]-1:intuple[2]+1] # may need to validate
    mid_range = file_lines[intuple[0]][intuple[1]-1] + file_lines[intuple[0]][intuple[2]]
    lower_range = file_lines[intuple[0]+1][intuple[1]-1:intuple[2]+1]
    char_string = upper_range + mid_range + lower_range
    return any(char in char_string for char in special_chars)

def gen_digits_locs(lines: str) -> list:
    ddd_list = []
    for idx,i in enumerate(lines):
        for m in re.finditer('\d{1,3}',i):
            ddd_list.append((idx, m.start(),m.end()))
    return ddd_list

if __name__ == "__main__":

    with open('day3AData.txt') as f:
        lines = f.readlines(0)
    padded_lines = pad_lines(lines)
    special_chars = get_unique_chars(padded_lines)
    num_locs = gen_digits_locs(padded_lines)
    parts = []
    for n, number in enumerate(num_locs):
        if include_part(number,padded_lines,special_chars):
            parts.append(int(padded_lines[number[0]][number[1]:number[2]]))
    print(sum(parts))

