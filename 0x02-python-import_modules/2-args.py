#!/usr/bin/python3
# import sys

"__name__" == "__main__"
import sys

iterate = len(sys.argv) - 1
if (iterate == 0):
    print("0 argument.")
elif (iterate == 1):
    print("1 argument:")
else:
    print("{} arguments:".format(iterate))
for args in range(iterate):
    count = args + 1
    print("{}: {}".format(count, sys.argv[count]))