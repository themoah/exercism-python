def distance(firstWord, secondWord):
    if (len(firstWord) != len(secondWord)): raise ValueError("ValueError")
    hummingCounter = 0
    for i in range(0, len(firstWord)):
         if (firstWord[i] != secondWord[i]): hummingCounter += 1
    return hummingCounter
