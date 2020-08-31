import sys

list = sys.argv[1:]
str = ' '.join(list).swapcase()[::-1]

print(str)
