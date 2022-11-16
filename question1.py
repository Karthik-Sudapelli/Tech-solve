import decimal
from decimal import Decimal, getcontext


def large_small_number(value: list
                       ) -> tuple:
    value.sort()
    return value[0], value[len(value) - 1]


if __name__ == '__main__':
    numeric_value = []
    while True:
        numeric_value.clear()
        user_input = input("enter list of integers")
        user_input_split = user_input.split()
        getcontext().prec = 4
        exit_outer_loop: bool = True
        for value in user_input_split:
            try:
                numeric_value.append(Decimal(value))
            except decimal.InvalidOperation:
                print("Invalid input")
                exit_outer_loop = False
                break
        if exit_outer_loop:
            break
    small_, large_ = large_small_number(numeric_value)
    print(f'\nlargest number is {large_} and smallest numer is {small_}')
