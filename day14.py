def process_memory(filename):
    mem = dict()
    with open(filename) as file:
        lines = file.readlines()
        mask = None
        for line in lines:
            line = line.strip()
            if line.startswith("mask"):
                mask = line.split(" = ")[1]
                print(mask)
            else:
                assignment = line.split(" = ")
                address = int(assignment[0][4:-1])
                value = int(assignment[1])
                mem[address] = apply_mask(mask, value)
    return mem


def apply_mask(mask, value):
    index = 35
    mask_or = 0
    mask_and = 0
    for c in mask:
        if c == '0':
            mask_and += 2 ** index
        if c == '1':
            mask_or += 2 ** index
        index -= 1

    return mask_or | value & ~mask_and


# mem_after = process_memory("resources/day14_test.txt")
mem_after = process_memory("resources/day14_input.txt")
print(mem_after)
print(f"Sum is {sum(mem_after.values())}")

