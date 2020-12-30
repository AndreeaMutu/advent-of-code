def load_seats(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def partition(seat, max_number, lower_ids=('F', 'L'), upper_ids=('B', 'R')):
    lower = 0
    upper = max_number
    for c in seat:
        if c in lower_ids:
            upper -= (upper - lower) // 2 + 1
        elif c in upper_ids:
            lower += (upper - lower) // 2 + 1
    return lower


def parse_seat_ids(filename):
    seat_ids = []
    seats = load_seats(filename)
    for seat in seats:
        seat = seat.strip()
        row = partition(seat[:7], 127)
        column = partition(seat[7:], 7)
        seat_ids.append(row * 8 + column)
    return seat_ids


# ids = parse_seat_ids("resources/day5_test.txt")
ids = parse_seat_ids("resources/day5_input.txt")
ids = sorted(ids)
print(ids)
print(max(ids))
my_seat = [ids[i]+1 for i in range(0, len(ids) - 1) if ids[i] == ids[i + 1] - 2]
print(my_seat)
