def prepare_bag(text: str):
    text = text.strip()
    if text.find('bags') != -1:
        return text.replace('bags', '').strip()
    if text.find('bag') != -1:
        return text.replace('bag', '').strip()
    return text


class Bag:

    def __init__(self, color, contents):
        self.color = color
        contents = contents.strip().replace('.', '')
        if contents == "no other bags":
            self.bags = {}
        else:
            self.bags = {prepare_bag(t)[2:]: int(prepare_bag(t)[0]) for t in contents.split(",")}

    def __str__(self) -> str:
        return f"{self.color}:{self.bags}"


def parse_bags(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        bags = []
        for line in lines:
            bag_contents = line.split("contain")
            bags.append(Bag(prepare_bag(bag_contents[0]), bag_contents[1]))

        return {bag.color: bag for bag in bags}


def bags_containing_color(bags, color):
    contains_color = set()
    for bag_color, bag in bags.items():
        if color in bag.bags:
            contains_color.add(bag_color)
            contains_color = contains_color.union(bags_containing_color(bags, bag_color))
        else:
            bags_to_check = {b: bags[b] for b in bag.bags if b in bags}
            contains_color = contains_color.union(bags_containing_color(bags_to_check, color))

    return contains_color


def count_bags_in_bag_of_color(bags, color):
    number_of_bags = 0
    color_bag = bags[color]
    for bag_color, number in color_bag.bags.items():
        count = 1
        if len(bags[bag_color].bags) > 0:
            count = count_bags_in_bag_of_color(bags, bag_color)
            number_of_bags += number
        number_of_bags += number * count
    return number_of_bags


# bags = parse_bags("resources/day7_test.txt")
bags = parse_bags("resources/day7_input.txt")
# for bag in bags.values():
#     print(bag, end=", ")

containing_color = bags_containing_color(bags, 'shiny gold')
# print(containing_color)
print(f"Number of colors containing shiny gold: {len(containing_color)}")
bags_in_bag_of_color = count_bags_in_bag_of_color(bags, 'shiny gold')
print(f"\nNumber of bags in shiny gold bag: {bags_in_bag_of_color}")
