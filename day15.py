def load_start_numbers(filename):
    with open(filename) as file:
        inputs = file.readlines()
        return [[int(number) for number in line.strip().split(",")] for line in inputs]


def find_nth_number(start_numbers, n):
    turn = 1
    current = 0
    latest_turns = dict()
    while turn <= n:
        if turn <= len(start_numbers):
            current = start_numbers[turn - 1]
            latest_turns[current] = turn, 1
        else:
            last_turn, count = latest_turns[current]
            if count == 1:
                current = 0
            else:
                current = last_turn - prev_turn
            if current in latest_turns:
                prev_turn, count = latest_turns[current]
                latest_turns[current] = turn, count + 1
            else:
                latest_turns[current] = turn, 1
        turn += 1
    return current


# numbers_list = load_start_numbers("resources/day15_test.txt")
numbers_list = load_start_numbers("resources/day15_input.txt")

# end = 2020
end = 30000000
for numbers in numbers_list:
    print(f"For {numbers} the {end}th number is: {find_nth_number(numbers, end)}")
