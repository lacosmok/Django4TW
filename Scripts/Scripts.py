import operator

"""
Wersja na pythona 2.0
Przy Pythonie 3.0 wystarczy zamienić raw_input() na input()
"""


def Exercise1():
    name = raw_input("please write ur name ")
    year = int(raw_input("please write year when u were born ")) + 100
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return (name, year, "leap year")
    else:
        return (name, year, "common year")


def Exercise2(name):
    file = open(name, "r")
    dictionary = {}
    for word in file.read().split():
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 0
    sorted_dict = sorted(dictionary.items(), key=operator.itemgetter(1))
    return (sorted_dict)


print(Exercise1())
print(Exercise2("lorem ipsum.txt"))
