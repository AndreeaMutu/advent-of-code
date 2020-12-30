def load_groups(filename):
    with open(filename, 'r') as file:
        text = file.read()
        groups = text.split("\n\n")
        return groups


def count_anyone(groups):
    sum_yes = 0
    for group in grps:
        group = set(group.replace("\n", ""))
        sum_yes += len(group)
    return sum_yes


def count_everyone(groups):
    sum_yes = 0
    for group in grps:
        answers = group.split("\n")
        if len(answers) == 1:
            sum_yes += len(answers.pop())
        else:
            pers_no = len(answers)
            all_answers_in_group = group.replace("\n", "")
            unique = set(all_answers_in_group)
            common_answers = {u: all_answers_in_group.count(u) for u in unique if
                              all_answers_in_group.count(u) == pers_no}
            sum_yes += len(common_answers)
    return sum_yes


# grps = load_groups("resources/day6_test.txt")
grps = load_groups("resources/day6_input.txt")
print(grps)
count_any = count_anyone(grps)
count_every = count_everyone(grps)
print(f"Count any {count_any}")
print(f"Count every {count_every}")
