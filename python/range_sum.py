# Given a range of numbers. Iterate from 0th number to the end number and
# print the sum of the current number and previous number

# Expected Output when num is 10
# 0
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17


def display_sum(end_num):
    previous_num = 0
    for num in range(end_num):
        sum = previous_num + num
        print(sum)
        previous_num = num


display_sum(10)
