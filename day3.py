
def map():
    file = "input.txt"
    with open(file, "r") as f:
        lines = f.readlines()

    table = {}
    numbers = {}
    gears = {}

    line_idx = 0
    number_idx = 0
    
    for line in lines:
        line_idx += 1
        char_idx = 0
        number_key = str(number_idx) + "|"
        number_value = []
        for char in line:
            char_idx += 1
            key = (line_idx, char_idx)
            table[key] = char

            if("*" in char):
                gears[key] = char

            if(char.isdigit()):
                number_key += char
                number_value.append(key)
                #print(number_key)
            else:
                if(number_key):
                    numbers[number_key] = number_value
                number_idx += 1
                number_key = str(number_idx) + "|"
                number_value = []

    #print(numbers)
    return [numbers, table, gears] 

[numbers, table, gears] = map()


def check_number(number, coords, gear = 0):
    #print("checking", number, coords)

    x_range = range(coords[0][0] - 1, coords[0][0] + 2)

    y_range = []
    for coord in coords:
        y_range.append(coord[1])
    
    y_range = range(min(y_range) - 1, max(y_range) + 2)

   # print("y_range", y_range)
    #print("x_range", x_range)


    for y in (y_range):
        #print("y", y)
        for x in x_range:
            #print("xy", x, y)
            if (x, y) in table:
                value = table[(x, y)]
                #print(x, y)
                #print(value)
                if(not value.isdigit() and not "." in value and not "\n" in value):
                    #print("adding", number)
                    return int(number)

    return 0

total = 0
ok_numbers = []

all_numbers = []

for number_split in numbers:
    number_array = number_split.split("|")
    number = number_array[1]
    #print(number_split)

    coords = (numbers.get(number_split))
    #print(coords)
    if(number) :
        #print('checking ', number_array[0], number, coords)
        all_numbers.append(number)
        result = check_number(number, coords)
        #result = 0
        if(result):
            ok_numbers.append(number_split)
            #print("number ok:", number)
            total += result
        #else:
            #print("not ok:", number, coords)
        #print (coords)

total_gear = 0

for gear in gears:

    gear_ratio = []

    #print(gear)
    gear_x_range = range(gear[0] - 1, gear[0] + 2)
    gear_y_range = range(gear[1] - 1, gear[1] + 2)

    for number_split in numbers:
        number_array = number_split.split("|")
        number = number_array[1]
        if number:
            #print(number_split)

            coords = (numbers.get(number_split))
            for coord in coords:
                if coord[0] in gear_x_range and coord[1] in gear_y_range:
                    #print("in", coord[0], coord[1], gear_x_range, gear_y_range)
                    if(number not in gear_ratio):
                        gear_ratio.append(number)
    
    if(len(gear_ratio) > 1):
        this_ratio = 1
        for g in gear_ratio:
            this_ratio *= int(g)
        
        total_gear += this_ratio





#coords = numbers.get("14|661")
#print(check_number(661, coords))

print("total", total)
if total <= 317301 or total >= 548169:
    print("too low/high")
#print("all", all_numbers)

print("total_gear", total_gear)


