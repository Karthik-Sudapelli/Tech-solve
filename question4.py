import re


def check_validity(value: str) -> bool:
    value = re.sub("[\s\-\.\*\(\)]*", "", value)
    match = re.search("^(\+?61|0|\+?610)?[2-57-8][0-9]{8}$", value)
    return not (match is None)


if __name__ == '__main__':
    user_input = str(input("enter your Australian phone number"))
    if check_validity(user_input):
        print("Valid number")
    else:
        print("Invalid, acceptable numbers -> 0xxxxxxxxx or +610xxxxxxxxx or 610xxxxxxxxx or xxxxxxxxx")
