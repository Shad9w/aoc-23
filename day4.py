file = "input.txt"
with open(file, "r") as f:
    lines = f.readlines()

part = 2

part1 = 0
part2 = 0

card_values = {}
card_copies = {}

for line in lines:
    line = line.replace("\n", "")
    card_parse = line.split(":")
    numbers = card_parse[1].split("|")

    card_id = int(card_parse[0].replace("Card ", ""))
    total = 0

    scratchcard = numbers[0].split(" ")

    for w in numbers[1].split(" "):
        if w:
            if w in scratchcard:
                if part == 1:
                    if total == 0:
                        total = 1
                    else:
                        total *= 2
                else:
                    total += 1
    card_values[card_id] = total
    card_copies[card_id] = 1
    part2 += 1
    part1 += total


def add_card_copies(card, count):
    global part2
    for i in range(0, count) :
        if(card_values[card] is not None):
            card_to_add = (i + card + 1)
            card_copies[card_to_add] += 1
            part2 += 1
            if card_values[card]:
                add_card_copies(card_to_add, card_values[card_to_add])

if part == 2:
    for c in card_values:
        if card_values[c]:
            add_card_copies(c, card_values[c])


print("part2", part1)
print("part1", part2)