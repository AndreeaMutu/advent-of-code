def evaluate(expression, precedence, stop_operator):
    output = []
    operator = ""

    for i in range(0, len(expression)):
        token = expression[i]
        if token.isnumeric():
            output.append(token)
        if i == len(expression) - 1 or token in "*+":
            if i == len(expression) - 1 or precedence.get(operator, -1) > precedence[token]:
                prev = output.pop()
                to_compute = []
                while len(output) > 0 and prev != stop_operator:
                    to_compute.insert(0, prev)
                    prev = output.pop()

                if prev == stop_operator:
                    output.append(prev)
                else:
                    to_compute.insert(0, prev)
                precedence_expr_result = get_result(to_compute)
                output.append(str(precedence_expr_result))
            operator = token
            output.append(token)
    return get_result(output)


def get_result(output):
    if len(output) >= 3:
        operand2 = output.pop(0)
        operator = output.pop(0)
        operand1 = output.pop(0)
        res = execute(operand1, operand2, operator)
        while len(output) >= 2:
            operator = output.pop(0)
            operand = output.pop(0)
            res = execute(operand, res, operator)
        return res
    else:
        return output[0]


def execute(operand1, operand2, operator):
    if operator == "+":
        return int(operand1) + int(operand2)
    else:
        return int(operand1) * int(operand2)


def compute(expr, precedence):
    if len(set(precedence.values())) != 1:
        stop_operator = "*"
    else:
        stop_operator = None
    expr = expr.strip().replace(" ", "")
    output = []
    for token in expr:
        if token.isnumeric():
            output.append(token)
        if token in "+*":
            output.append(token)

        if token == "(":
            output.append(token)
        if token == ")":
            prev_output_token = output.pop()
            to_compute = []
            while prev_output_token != "(":
                to_compute.insert(0, prev_output_token)
                prev_output_token = output.pop()
            sub_expr_result = evaluate(to_compute, precedence, stop_operator)
            output.append(str(sub_expr_result))

    result = evaluate(output, precedence, stop_operator)
    # print(result)
    return result


def solve_homework(filename, precedence={"+": 0, "*": 0}):
    with open(filename) as file:
        expressions = file.readlines()
        sum_results = 0
        for expr in expressions:
            sum_results += int(compute(expr, precedence))
        return sum_results


# part1_sum = solve_homework("resources/day18_test.txt")
part1_sum = solve_homework("resources/day18_input.txt")
print(f"Sum part 1 = {part1_sum}")

# part2_sum = solve_homework("resources/day18_test.txt", {"+": 1, "*": 0})
part2_sum = solve_homework("resources/day18_input.txt", {"+": 1, "*": 0})
print(f"Sum part 2 = {part2_sum}")
