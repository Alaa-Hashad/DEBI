def palindrome():

    s = input("Enter your value : ")
    re= s[::-1]

    if (s== re):
        print("Yes, it is palindrome")
    else:
            print("No, it is not palindrome")


def find_nth_occurrence(substring, string, occurrence=1):
    try:
        loc = 0
        for i in range(occurrence):
            loc = string.find(substring, loc)
            loc += 1

        return loc - 1
    except:
        print("Wrong input!")


import re

def solve(a,b):
    pattern = a.replace("*", ".*")
    return bool(re.fullmatch(pattern, b))