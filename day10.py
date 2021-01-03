def load_joltages(filename):
    with open(filename, 'r') as file:
        return [int(line) for line in file.readlines()]


def jolts_differences(joltages):
    differences = {}
    joltages = sorted(joltages)
    joltages.append(joltages[-1] + 3)
    print(joltages)
    adapter = 0
    for j in joltages:
        diff = j - adapter
        if diff in differences:
            differences[diff] += 1
        else:
            differences[diff] = 1
        adapter = j
    return differences


def count_possibilities(joltages):
    joltages = sorted(joltages)
    joltages.insert(0, 0)
    joltages.append(joltages[-1] + 3)
    possibilities = {0: 1}
    for j in joltages[1:]:
        # Each joltage route is equal to the sum of the number of routes to the previous three joltages.
        # However, some of the joltages won't be present in the list of adaptors.
        # So the number of routes to them will be 0.
        possibilities[j] = possibilities.get(j - 1, 0) + possibilities.get(j - 2, 0) + possibilities.get(j - 3, 0)

    return possibilities[joltages[-1]]


# joltages = load_joltages("resources/day10_test.txt")
joltages = load_joltages("resources/day10_input.txt")
differences = jolts_differences(joltages)
print(differences)
print(f"1 diff * 3 diff: {differences[1] * differences[3]}")

print(f"Part 2 number of possibilities {count_possibilities(joltages)}")