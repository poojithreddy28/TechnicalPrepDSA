def countDictionary(words):
	count = {}
	for word in words:
		if word in count:
			count[word] += 1
		else:
			count[word] = 1
	print(count)
	


words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
countDictionary(words)
