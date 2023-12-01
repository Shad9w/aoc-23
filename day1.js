async function get_input(){
    try {
        const response = await fetch("input.txt")
        const text = await response.text();
        return text;
    }
    catch (error) {
        throw error;
    }
}

function isInteger(str) {
    return /^\d+$/.test(str);
}

async function part2()
{
    text = await get_input()
    lines = text.split('\n');
    total = 0;

    new_text = ""
    w_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9};

    for(l in lines)
    {
        
        last = null;
        first = null;

        line = lines[l];
        line_left_start = "";
        line_left_end = "";

        char_idx = 0;
        for(char in line){
            char_idx++;
            if(isInteger(line[char]))
            {
                last = line[char]
                if(first === null){
                    first = last
                    if(char_idx >= 3)
                    {
                        line_left_start = line.slice(0, char_idx);
                        console.log('re-checking first', line_left_start, char_idx)
                    }
                    console.log('first set to ', first)
                }
                
                line_left_end = line.slice(char_idx, line.length);
                console.log('re-checking last', line_left_end, char_idx)

                console.log(line[char])

            }
        }

        if(!first){
            line_left_start = line_left_end = line;
        }

        first_match = line_left_start.match(/one|two|three|four|five|six|seven|eight|nine/g)
        if(first_match){
            first = (w_numbers[first_match[0]])
            console.log('first', first)
        }

        last_match = line_left_end.split("").reverse().join("").match(/eno|owt|eerht|ruof|evif|xis|neves|thgie|enin/g)
        if(last_match){
            last = (w_numbers[last_match[0].split("").reverse().join("")])
            console.log("last", last)
        }

        number = parseInt(first) * 10 + parseInt(last)
        console.log(line, '|' , first , last, number)
        if(isInteger(number))
            total = total + number
    }

    console.log('total', total)

}

part2()
