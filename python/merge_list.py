# Given a two list of ints create a third list such that
# should contain only odd numbers from the first list and
# even numbers from the second list

# Expected Output
# listOne = [10, 20, 23, 11, 17]
# listTwo = [13, 43, 24, 36, 12]

# Merged List is
# [23, 11, 17, 24, 36, 12]


def merge_list(list1, list2):
    new_list = []

    for num in list1:
        if num % 2 != 0:
            new_list.append(num)

    for num in list2:
        if num % 2 == 0:
            new_list.append(num)

    return new_list


listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

print("Merged List is")
print(merge_list(listOne, listTwo))
