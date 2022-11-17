from collections import OrderedDict


# uncomment @profile and use terminal command kernprof -l -v question2.py to time complexties after installing -> pip install
# @profile
def solution1(value: str) -> str:
    length_value = len(value)
    dummy_value = ""

    for pos in range(length_value):
        if value[pos] not in dummy_value:
            dummy_value = dummy_value.__add__(value[pos])
    return dummy_value


# @profile
def solution2(value: str) -> str:
    return "".join(sorted(set(value), key=value.index))


# @profile
def solution3(value: str) -> str:
    return "".join(OrderedDict.fromkeys(value))


if __name__ == '__main__':
    user_input: str = str(input("enter string"))
    while True:
        user_input_choice = str(input("which solver you want use 1 2 3 (only enter a digit)"))
        if len(user_input_choice) == 1 and user_input_choice.isdigit():
            solver_choice_dict = {"1": solution1, "2": solution2, "3": solution3}
            print(f"input after removing duplicate using solution1 is {solver_choice_dict[user_input_choice](user_input)}")
            break
        print("Invalid\n")
