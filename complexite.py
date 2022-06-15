# #max result
# n = 1000

# result = 123 +42


# numbers =[123, 42, 3.14]

# for number in numbers:
#     result = number * 2
#     print(result)

# more_numbers = [2.71, 3.14, 0, 53]
# common_numbers = []

# for number in numbers:
#     for more_number in more_numbers:
#         if number == more_number:
#             common_numbers.append(number)
# print(common_numbers)

# result = 0
# matrix = [
#     [123, 42, 3.14],
#     [2.71, 3.14, 0],
#     [1, 2, 3]
# ]

# for line in matrix:
#     for number in line:
#         result = number*2
#         print(result)

# words = ["ananas", "banane", "cerise", "durian", "kiwi", "orange", "pomme"]

###exo 1    determiner la complexite algorithmique de ce programme
#O(?)   rep: O(n)

numbers = [4, 10, 42, 3.14]
my_list = []

while True:
    number = number.pop()
    my_list.append(number)

    if len(numbers) == 0:
        break



###exo2     determiner la complexite algorithmique de ce programme
#O(?)       rep: O(n)

numbers = [4, 10, 42, 3.14]
my_list = []

for n in numbers:
    result = n**2       #puissance 2
    my_list.append(result)