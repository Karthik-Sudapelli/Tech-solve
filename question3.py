def anagram_check(value1: str, value2: str) -> bool:
    if len(value1) == len(value2) and sorted(("".join(set(value1))).casefold()) == sorted("".join((set(value2))).casefold()):
        return True
    else:
        return False


if __name__ == '__main__':
    user_input1: str = str(input("enter first string"))
    user_input2: str = str(input("enter second string"))
    print(f"Both strings are {anagram_check(user_input1, user_input2)} anagram")
