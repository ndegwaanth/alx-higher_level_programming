#!/usr/bin/python3
for number in range(0, 100):
    if (number <= 0 or number <= 9):
        print(" {:02}".format(number), end=",")
    else:
        print(f" {number}", end=",")
