def valid_range(r):
    start_stop = r.split("-")
    return range(int(start_stop[0]), int(start_stop[1]) + 1)


class Rule:

    def __init__(self, rule):
        split = rule.strip().split(": ")
        self.field = split[0]
        self.ranges = [valid_range(r) for r in split[1].split(" or ")]

    def is_valid(self, number):
        for rng in self.ranges:
            if number in rng:
                return True
        return False


class Tickets:
    def __init__(self, rules, my_ticket, nearby_tickets):
        self.rules = [Rule(rule) for rule in rules]
        self.my_ticket = [int(t) for t in my_ticket.strip().split(",")]
        self.nearby_tickets = [[int(t) for t in n.strip().split(",")] for n in nearby_tickets]

    def is_valid_value(self, value):
        for rule in self.rules:
            if rule.is_valid(value):
                return True
        return False

    def ticket_scanning_error_rate(self):
        error_rate = 0
        for ticket in self.nearby_tickets:
            for value in ticket:
                if not self.is_valid_value(value):
                    error_rate += value
        return error_rate

    def valid_tickets(self):
        valid_nearby_tickets = []
        for ticket in self.nearby_tickets:
            valid = True
            for value in ticket:
                if not self.is_valid_value(value):
                    valid = False
            if valid:
                valid_nearby_tickets.append(ticket)
        return valid_nearby_tickets

    def all_valid_rules(self, value):
        valid_rules = set()
        for rule in self.rules:
            if rule.is_valid(value):
                valid_rules.add(rule.field)

        return valid_rules

    def identify_order(self):
        fields_by_index = {}
        for ticket in self.valid_tickets():
            for i in range(len(ticket)):
                valid_rules = self.all_valid_rules(ticket[i])
                if i in fields_by_index:
                    fields_by_index[i] = fields_by_index[i].intersection(valid_rules)
                else:
                    fields_by_index[i] = valid_rules
        field_index_pairs = {}
        while len(fields_by_index) > len(field_index_pairs):
            for index, fields in fields_by_index.items():
                for item in field_index_pairs:
                    fields.discard(item)
                if len(fields) == 1:
                    field_index_pairs[fields.pop()] = index

        return field_index_pairs

    def my_ticket_fields(self):
        fields_order = self.identify_order()
        return {field: self.my_ticket[index] for (field, index) in fields_order.items()}


def load_tickets(filename):
    with open(filename) as file:
        text = file.read()
        sections = text.split("\n\n")
        rules_section = sections[0].split("\n")
        my_ticket = sections[1].split(":")[1].strip()
        nearby_tickets = sections[2].split(":\n")[1].split("\n")
        return Tickets(rules_section, my_ticket, nearby_tickets)


# tickets = load_tickets("resources/day16_test.txt")
# tickets = load_tickets("resources/day_16_test_valid.txt")
tickets = load_tickets("resources/day16_input.txt")
print(f"Tickets scanning error rate: {tickets.ticket_scanning_error_rate()}")
fields = tickets.my_ticket_fields()
print(f"My ticket fields: {fields}")
departure_product = 1
for field, value in fields.items():
    if field.startswith("departure"):
        departure_product *= value
print(f"departure product: {departure_product}")
