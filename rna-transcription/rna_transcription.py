def to_rna(testPhrase):
    dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    response = ''
    listOfLetters = list(testPhrase)
    for char in listOfLetters:
        if dict.has_key(char):
            response += dict[char]
        else:
            return ''
    return response
