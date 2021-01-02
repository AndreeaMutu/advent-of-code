def load_numbers(filename):
    with open(filename, 'r') as file:
        return [int(line) for line in file.readlines()]


def is_valid(current, numbers, start, end):
    for i in range(start, end - 1):
        for j in range(i + 1, end):
            if numbers[i] != numbers[j] and numbers[i] < current and \
                    numbers[j] < current and numbers[i] + numbers[j] == current:
                return True
    return False


def find_number_not_valid(numbers, preamble):
    start = 0
    end = preamble
    for i in range(preamble, len(numbers)):
        current = numbers[i]
        if not is_valid(current, numbers, start, end):
            return current
        start += 1
        end += 1
    return None


def contiguous_numbers_with_sum(numbers, invalid_number, interval_size):
    i = 0
    while i < len(numbers) - interval_size:
        numbers_to_test = [n for n in numbers[i:i + interval_size] if n < invalid_number]
        if len(numbers_to_test) == interval_size and sum(numbers_to_test) == invalid_number:
            return numbers_to_test
        i += 1
    return None


# numbers = load_numbers("resources/day9_test.txt")
# preamble = 5
numbers = load_numbers("resources/day9_input.txt")
preamble = 25

first_not_valid = find_number_not_valid(numbers, preamble)
print(f"First not valid number {first_not_valid}")
# 22477624

interval = 2

while interval <= len(numbers):
    contiguous = contiguous_numbers_with_sum(numbers, first_not_valid, interval)
    if contiguous is not None:
        encryption_weakness = min(contiguous) + max(contiguous)
        print(f"encryption weakness: {encryption_weakness}")
        break
    interval += 1
