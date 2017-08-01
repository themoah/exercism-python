def is_pangram(testPhrase):
	allLetters = set("thequickbrownfoxjumpsoverthelazydog")
	listOfChars = []
	testPhraseLower = testPhrase.lower()
	for char in testPhraseLower:
		if char.isalpha():
			listOfChars += char
	if (set(listOfChars) == allLetters):    	return True
	else:		return False
