def calculator(operation, value1, value2):
    if operation == "+": return value1 + value2
    if operation == "-": return value1 - value2
    if operation == "*": return value1 * value2
    if operation == "/": return value1 / value2

print(calculator("*", 10, 5))
