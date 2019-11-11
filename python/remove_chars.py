# Given a string and an int n, remove characters from string
# starting from zero up to n and return a new string

# Expected Output
# Removing n number of chars
# tive


def remove_chars(data, n):
    if n > len(data):
        print("Given number exceeds length of string.")
        exit()

    return data[n:]


string = "pynative"
n = 10
print("Removing {} number of chars from {}".format(n, string))
string = remove_chars(string, n)
print(string)
