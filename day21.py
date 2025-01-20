with open("input_day21.txt") as myfile:
    lines = myfile.read().strip().split("\n")


monkey_operations = {}

for line in lines:
    to_divide = line.split(" ")
    monkey = to_divide[0][:-1]
    if len(to_divide) == 2:
        monkey_operations[monkey] = int(to_divide[1])
    else:
        monkey_operations[monkey] = to_divide[1:]


def OperateMonkeys(monkey_name):
    if isinstance(monkey_operations[monkey_name], int):
        return monkey_operations[monkey_name]
    to_divide = monkey_operations[monkey_name]
    right_monkey = OperateMonkeys(to_divide[2])
    left_monkey = OperateMonkeys(to_divide[0])


    return eval(f"{left_monkey}{to_divide[1]}{right_monkey}")


result = OperateMonkeys("root")
print(int(result))
monkey_operations.clear()

# Part two

from sympy import symbols, solve_linear   #(https://www.google.com/search?q=sympy+solve+linear+python&rlz=1C1SQJL_trTR923TR923&oq=&aqs=chrome.0.35i39i362l8.158768j0j7&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:a712434b,vid:UbuBwHbZTU8)
from sympy.parsing.sympy_parser import parse_expr #(https://stackoverflow.com/questions/33606667/from-string-to-sympy-expression)

with open("input_day21.txt") as myfile:
    lines = myfile.read().strip().split("\n")

key = symbols("humn")
monkey_operations = {}

for line in lines:
    to_divide = line.split(" ")
    monkey = to_divide[0][:-1]

    if len(to_divide) == 2:
        monkey_operations[monkey] = int(to_divide[1])
    else:
        monkey_operations[monkey] = to_divide[1:]


def OperateMonkeys2(monkey_name):
    if monkey_name == "humn":
        return key

    if isinstance(monkey_operations[monkey_name], int):
        return monkey_operations[monkey_name]
    to_divide = monkey_operations[monkey_name]
    right_monkey = OperateMonkeys2(to_divide[2])
    left_monkey = OperateMonkeys2(to_divide[0])


    return parse_expr(f"({left_monkey}){to_divide[1]}({right_monkey})")


left_monkey = OperateMonkeys2(monkey_operations["root"][0])
right_monkey = OperateMonkeys2(monkey_operations["root"][2])

result = solve_linear(left_monkey, right_monkey)[1]
print(result)