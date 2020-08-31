import sys
import string

def filter():
 
    word = sys.argv[1]
    nb = sys.argv[2]
    liste = word.split(" ")
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    delchar = ""
    for char in word:
        if char not in punctuations:
            delchar += char
    word = delchar
    liste = delchar.split(" ")
    for x in reversed(liste):
        if len(x) <= nb:
            liste.remove(x)
    liste = word.split(" ")
    print(liste)
filter()
