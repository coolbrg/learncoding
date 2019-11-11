# Accept string from the user and display only
# those characters which are present at an even index

# Expected Output
# Enter String: pynative
# Original String is pynative
# Printing only even index chars
# index[0] p
# index[2] n
# index[4] t
# index[6] v


def show_even_chars(data):
    print("Printing only even index chars")
    for i in range(0, len(data)-1, 2):
        print("index[{}] {}".format(i, data[i]))


string = input("Enter String: ")
print("Original String is {}".format(string))
show_even_chars(string)
