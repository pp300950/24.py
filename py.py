from itertools import permutations, product

def find_expression(numbers):
    operators = ['+', '-', '*', '/']
    number_permutations = permutations(numbers)
    for num_permutation in number_permutations:
        for ops in product(operators, repeat=3):
            expression = f"({num_permutation[0]}{ops[0]}{num_permutation[1]}){ops[1]}({num_permutation[2]}{ops[2]}{num_permutation[3]})"
            try:
                result = eval(expression)
                if result == 24:
                    print(f"นำเลข {num_permutation} และเครื่องหมาย {ops} มารวมกันได้ 24 ด้วยสมการ: {expression}")
                    return
            except ZeroDivisionError:
                pass
numbers = [4, 9, 11, 12]
find_expression(numbers)
