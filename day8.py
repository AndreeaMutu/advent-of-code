class Instruction:

    def __init__(self, instr: str):
        instruction = instr.split(" ")
        self.type = instruction[0]
        self.offset = int(instruction[1])
        self.has_run = False

    def __str__(self) -> str:
        return f"{self.type}: {self.offset} (run {self.has_run})"

    def run(self, acc):
        self.has_run = True
        if self.type == "nop":
            return +1
        if self.type == "acc":
            return +1
        return self.offset

    def swap(self):
        if self.type == "nop":
            self.type = "jmp" if self.offset != 0 else "nop"
        elif self.type == "jmp":
            self.type = "nop"

    def can_be_swapped(self):
        return (self.type == "nop" and self.offset != 0) or self.type == "jmp"

    def __eq__(self, o) -> bool:
        return self.type == o.type and self.offset == o.offset


def load_instructions(filename):
    with open(filename, 'r') as file:
        instructions = []
        for line in file:
            instr = Instruction(line.strip())
            instructions.append(instr)
        return instructions


def run_instructions(instructions):
    acc = 0
    i = 0
    current = instructions[i]
    while not current.has_run:
        # print(f"{current}")
        next_instr = current.run(acc)
        i += next_instr
        if current.type == "acc":
            acc += current.offset
        current = instructions[i]
    # print(f"{current}")
    return acc


def run_instructions_part2(instructions, swapped_instr):
    acc = 0
    i = 0
    no_swap = True
    while i < len(instructions):
        current = instructions[i]
        if current.has_run:
            return False, acc
        # print(f"{current}")
        if current.can_be_swapped() and current not in swapped_instr and no_swap:
            swapped_instr.append(Instruction(current.type + " " + str(current.offset)))
            current.swap()
            # print(f"swapped {current}")
            no_swap = False

        next_instr = current.run(acc)
        i += next_instr
        if current.type == "acc":
            acc += current.offset
    return True, acc


def copy_instr(instructions):
    return [Instruction(i.type + " " + str(i.offset)) for i in instructions]


# loaded_instr = load_instructions("resources/day8_test.txt")
loaded_instr = load_instructions("resources/day8_input.txt")

# for instr in loaded_instr:
#     print(instr, end=", ")

last_acc = run_instructions(loaded_instr)
print(f"\nacc part 1 = {last_acc}")

swapped = []
res = False
run = 0
while res is False:
    # print(f"Run {run}")
    res, last_acc2 = run_instructions_part2(copy_instr(loaded_instr), swapped)
    run += 1
print(f"\nacc part 2 = {last_acc2}")
