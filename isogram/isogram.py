def is_isogram(word):
	listOfChars = []
	charrArray = list(word.lower())
	for char in charrArray:
		if char.isalpha():
			listOfChars += char
	if (len(set(listOfChars)) != len(listOfChars)): return False
	else: return True
