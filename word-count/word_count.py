import collections

def word_count(args):
    convertArgsToString = str(args)
    listOfChars = ''
    for char in list(convertArgsToString):
        if char.isalpha() or char.isdigit():
            listOfChars += char.lower()
        else:
            listOfChars += ' '

    listOfCharsWithOutSpaces = " ".join(listOfChars.split())
    parsedArgs = listOfCharsWithOutSpaces.split(' ')
    count = collections.Counter(parsedArgs)
    return count
