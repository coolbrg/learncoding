# Command line program to say some message from the command prompt
# Output:
# $ python3 cmd_line.py 'Hello World'
#   Hello, World
# $ python3 cmd_line.py 'Hello your name.' 'How are you'
#   Hello, your name. How are you
# Hint: Use " ".join(sys.argv[1:]) to capture the rest of arguments into
# a string
import sys

if len(sys.argv) < 2:
    print("You forgot to enter the message.")
elif len(sys.argv) >= 2:
    print("Message is: {}".format(" ".join(sys.argv[1:])))
else:
    print("Just chill!")
