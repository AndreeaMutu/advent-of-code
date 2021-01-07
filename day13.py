def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        earliest_time = int(lines[0].strip())
        buses = list(filter(lambda bus: bus != 'x', lines[1].strip().split(",")))
        buses = [int(bus) for bus in buses]
        return earliest_time, buses


def part_1(earliest_time, buses):
    bus = None
    min_time = earliest_time
    while bus is None:
        bus = next(filter(lambda bus_id: min_time % bus_id == 0, buses), None)
        if bus is None:
            min_time += 1
    return bus * (min_time - earliest_time)


# time, available_buses = parse_input("resources/day13_test.txt")
time, available_buses = parse_input("resources/day13_input.txt")

print(time)
print(available_buses)

print(part_1(time, available_buses))
