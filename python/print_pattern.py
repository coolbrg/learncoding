# Print following pattern for given n as 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


def print_pattern(n):
    for i in range(n):
        for _ in range(0, i+1):
            print(i+1, end=" ")
        print()


print_pattern(5)
