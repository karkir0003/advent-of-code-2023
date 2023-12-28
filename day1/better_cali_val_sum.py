"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

def get_accurate_number(line):
    """
    Taking into account "spelled digits", get first and last digit
    """
    spelled_digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    first_digit = None 
    last_digit = None
    for i in range(len(line)):
        if (line[i].isdigit()):
            first_digit = int(line[i])
            break 
        else:
            for word in spelled_digits.keys():
                if (line.startswith(word, i)):
                    print(f'hit and word is {word} starting at index {i}')
                    first_digit = spelled_digits[word]
                    break
            if (first_digit):
                break
    
    for j in range(len(line) - 1, 0, -1):
        if (line[j].isdigit()):
            last_digit = int(line[j])
            break 
        else:
            for word in spelled_digits.keys():
                if (line.startswith(word, j)):
                    last_digit = spelled_digits[word]
                    break 
            if (last_digit):
                break
    if (first_digit is None):
        return 0
    elif (last_digit is None):
        last_digit = first_digit
    return first_digit * 10 + last_digit

def better_calc_sum_cali_values(path = "input.txt"):
    total = 0
    with open(path, "r") as f:
        for line in f.readlines():
            print(f'line: {line}')
            print(f'number: {get_accurate_number(line)}')
            total = total + get_accurate_number(line)
    return total


def main():
    #print(get_accurate_number('ninesevensrzxkzpmgz8kcjxsbdftwoner'))
    print(f'total calibration value: {better_calc_sum_cali_values()}')

if __name__ == '__main__':
    main()