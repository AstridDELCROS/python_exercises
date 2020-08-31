def display_intro():
    phrase = "The right format"
    char = '-'
    print("{}{}".format(char*(42 - (len(phrase))), phrase))
display_intro()
