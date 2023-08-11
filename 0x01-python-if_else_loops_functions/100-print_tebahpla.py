#!/usr/bin/python3
for i in range(90, 66):
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i + 32)), end="")
