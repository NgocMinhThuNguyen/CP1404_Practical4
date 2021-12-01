import random

NUMBER_EACH_LINE = 6
MINIMUM = 1
MAXIMUM = 45

number_of_lines = int(input("How many quick picks? "))
for i in range(number_of_lines):
    numbers = []
    for j in range(NUMBER_EACH_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in numbers:
            number = random.randint(MINIMUM, MAXIMUM)
        numbers.append(number)
    numbers.sort()

    for number in numbers:
        print(f"{number:>2}", end=" ")
    print()


