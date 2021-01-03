class Seat:
    def __init__(self, symbol):
        if symbol == 'L':
            self.is_empty = True
            self.is_floor = False
        elif symbol == '#':
            self.is_empty = False
            self.is_floor = False
        else:
            self.is_floor = True
            self.is_empty = None

    def __eq__(self, o) -> bool:
        return self.is_floor == o.is_floor and self.is_empty == o.is_empty

    def __str__(self) -> str:
        return "L" if self.is_empty else "." if self.is_floor else "#"

    def is_occupied(self):
        return not self.is_floor and not self.is_empty

    def copy_seat(self, is_changed=False):
        if self.is_floor:
            return Seat(".")
        if self.is_occupied():
            return Seat("L") if is_changed else Seat("#")
        return Seat("#") if is_changed else Seat("L")


def load_seats(filename):
    with open(filename) as file:
        rows = [[Seat(symbol) for symbol in line.strip()] for line in file.readlines()]
    return rows


def find_occupied(i, j, seats):
    occupied_neighbours = []
    indexes = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
               (i + 1, j + 1)]

    for tup in indexes:
        check_neighbour(tup[0], tup[1], occupied_neighbours, seats)
    return occupied_neighbours


def find_occupied_visible(i, j, seats):
    occupied_neighbours = []
    indexes = [(- 1, - 1), (- 1, 0), (- 1, + 1), (0, - 1), (0, + 1), (+ 1, - 1), (+ 1, 0),
               (+ 1, + 1)]
    indexes = [indexes_to_check(i, j, seats, idx) for idx in indexes]

    for tup in indexes:
        check_neighbour(tup[0], tup[1], occupied_neighbours, seats)
    return occupied_neighbours


def indexes_to_check(i, j, seats, change_tup):
    check_i = i + change_tup[0]
    check_j = j + change_tup[1]
    while 0 <= check_i < len(seats) and 0 <= check_j < len(seats[check_i]) and seats[check_i][check_j].is_floor:
        check_i = check_i + change_tup[0]
        check_j = check_j + change_tup[1]
    return check_i, check_j


def apply_rules(seats, occupied_function=find_occupied, min_occupied=4):
    changed_seats = [["." for seat in row] for row in seats]
    for i in range(0, len(seats)):
        for j in range(0, len(seats[i])):
            occupied_neighbours = occupied_function(i, j, seats)
            current_seat = seats[i][j]
            if current_seat.is_floor:
                changed_seats[i][j] = (current_seat.copy_seat())
            elif current_seat.is_occupied() and len(occupied_neighbours) >= min_occupied:
                changed_seats[i][j] = (current_seat.copy_seat(True))
            elif not current_seat.is_occupied() and len(occupied_neighbours) == 0:
                changed_seats[i][j] = (current_seat.copy_seat(True))
            else:
                changed_seats[i][j] = (current_seat.copy_seat())
    return changed_seats


def check_neighbour(i, j, occupied_neighbours, seats):
    if 0 <= i < len(seats) and 0 <= j < len(seats[i]) and seats[i][j].is_occupied():
        occupied_neighbours.append(seats[i][j])


def print_seats(rows):
    print()
    for row in rows:
        for seat in row:
            print(seat, end="")
        print()


def count_occupied(rows):
    occ = 0
    for row in rows:
        for seat in row:
            if seat.is_occupied():
                occ += 1
    return occ


# seat_rows = load_seats("resources/day11_test.txt")
seat_rows = load_seats("resources/day11_input.txt")
# print_seats(seat_rows)

# part 1
# initial = seat_rows
# changed = apply_rules(initial)
# while initial != changed:
#     # print_seats(changed)
#     initial = changed
#     changed = apply_rules(initial)

# part 2
initial = seat_rows
changed = apply_rules(initial, find_occupied_visible, 5)
while initial != changed:
    # print_seats(changed)
    initial = changed
    changed = apply_rules(initial, find_occupied_visible, 5)

print(f"Occupied seats: {count_occupied(changed)}")
