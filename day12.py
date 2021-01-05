class Ship:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "E"

        self.wp_x = 10
        self.wp_y = 1

    def move(self, action: str):
        instruction = action[0]
        value = int(action[1:])
        if instruction in "LR":
            self.direction = self.__change_direction(instruction, value)
        elif instruction in "NESW":
            self.move_in_direction(instruction, value)
        else:
            self.move_in_direction(self.direction, value)

    def move_in_direction(self, instruction, value):
        if instruction == 'N':
            self.y += value
        elif instruction == 'S':
            self.y -= value
        elif instruction == 'E':
            self.x += value
        elif instruction == 'W':
            self.x -= value

    def move_wp_in_direction(self, instruction, value):
        if instruction == 'N':
            self.wp_y += value
        elif instruction == 'S':
            self.wp_y -= value
        elif instruction == 'E':
            self.wp_x += value
        elif instruction == 'W':
            self.wp_x -= value

    def __change_direction(self, instruction, value):
        coords = "NESW"
        turn_value = value // 90
        point_index = coords.index(self.direction)
        if instruction == "R":
            return coords[(point_index + turn_value) % 4]
        else:
            return coords[point_index - turn_value]

    def manhattan_dist_part1(self):
        return abs(self.x) + abs(self.y)

    def move_part2(self, action: str):
        instruction = action[0]
        value = int(action[1:])
        if instruction in "NESW":
            self.move_wp_in_direction(instruction, value)
        elif instruction in "LR":
            self.rotate_waypoint(instruction, value)
        else:
            self.x += value * self.wp_x
            self.y += value * self.wp_y

    def rotate_waypoint(self, instruction, value):
        if instruction == 'R':
            angle = 360 - value
        elif instruction == 'L':
            angle = value

        if angle == 90:
            helper = self.wp_x
            self.wp_x = -1 * self.wp_y
            self.wp_y = +1 * helper
        elif angle == 180:
            self.wp_x = -1 * self.wp_x
            self.wp_y = -1 * self.wp_y
        elif angle == 270:
            helper = self.wp_x
            self.wp_x = +1 * self.wp_y
            self.wp_y = -1 * helper


def compute_dist(filename):
    ship = Ship()
    with open(filename) as file:
        for line in file.readlines():
            ship.move(line.strip())

    return ship.manhattan_dist_part1()


def compute_dist_part2(filename):
    ship = Ship()
    with open(filename) as file:
        for line in file.readlines():
            ship.move_part2(line.strip())

    return ship.manhattan_dist_part1()


# dist = compute_dist("resources/day12_test.txt")
# Part 1
dist = compute_dist("resources/day12_input.txt")

print(f"Manhattan distance part 1 = {dist}")

# dist2 = compute_dist_part2("resources/day12_test.txt")
# Part 2
dist2 = compute_dist_part2("resources/day12_input.txt")

print(f"Manhattan distance part 2 = {dist2}")