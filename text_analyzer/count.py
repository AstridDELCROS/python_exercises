def text_analyzer(text='default value: hello test'):
    ''' This function counts the number of upper characters, lower characters,    punctuation and spaces in a given text.'''
    letters = 0
    numbers = 0
    spaces = 0
    others = 0
    if text == "":
        exit("What is the text to analyze?")
    for x in text:
        if x.isalpha():
            letters += 1
        elif x.isdigit():
            numbers += 1
        elif x.isspace():
            spaces += 1
        else:
            others +=1
    total = letters + numbers + spaces + others
    print("The text contains " + str(total) + " characters")
    print("- %d letters"%(letters))
    print("- {} numbers".format(numbers))
    print("- {} spaces".format(spaces))
    print("- {} ponctuation marks".format(others))
