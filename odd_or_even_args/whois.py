import sys

list = sys.argv
len = len(list)
if len != 2 or not list[1].isdigit():
    exit("ERROR")
x = int(list[1])
if x % 2 == 0 and x != 0:
    print("I'm even")
elif x == 0:
    print("I'm zero")
else:
    print ("I'm odd")
