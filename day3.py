class Slope:

    def __init__(self, trees, size):
        self.trees = trees
        self.size = size

    def is_tree(self, pos):
        return pos % self.size in self.trees


def parse_file(file_name):
    map_config = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            trees = [i for i in range(0, len(line)) if line[i] == '#']
            map_config.append(Slope(trees, len(line)))
    return map_config


def trees_on_map(map_config, right, down=1):
    trees_no = 0
    for i in range(down, len(map_config), down):
        location = (i / down) * right
        if map_config[i].is_tree(location):
            trees_no += 1

    return trees_no


# map_trees = parse_file("resources/day3_p1_test.txt")
map_trees = parse_file("resources/day3_p1_input.txt")
number_of_trees_1 = trees_on_map(map_trees, 1)
number_of_trees_3 = trees_on_map(map_trees, 3)
number_of_trees_5 = trees_on_map(map_trees, 5)
number_of_trees_7 = trees_on_map(map_trees, 7)
number_of_trees_1_2 = trees_on_map(map_trees, 1, 2)
print(f"We have {number_of_trees_1} trees for Right 1, down 1")
print(f"We have {number_of_trees_3} trees for Right 3, down 1")
print(f"We have {number_of_trees_5} trees for Right 5, down 1")
print(f"We have {number_of_trees_7} trees for Right 7, down 1")
print(f"We have {number_of_trees_1_2} trees for Right 1, down 2")
print(
    f"Multiplied {number_of_trees_1 * number_of_trees_3 * number_of_trees_5 * number_of_trees_7 * number_of_trees_1_2}")
