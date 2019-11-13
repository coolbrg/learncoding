import sys

something_went_wrong = True

if something_went_wrong:
    print("Oh! This is a nice line", file=sys.stdout)
    print("Oh crap! Something went wrong.", file=sys.stderr)
    sys.exit(1)

# Demo stdout as $ cat 0< file_name or simply $ cat < file_name
