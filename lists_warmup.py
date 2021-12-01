numbers = [3, 1, 4, 1, 5, 9, 2]

# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(numbers)

# 2. Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)

# 3. Get all the elements from numbers except the first two (slice)
new_numbers = numbers[2:]
print(new_numbers)

# 4. Check if 9 is an element of numbers
if 9 in numbers:
    print("9 is an element of numbers")
else:
    print("9 is not an element of numbers")
