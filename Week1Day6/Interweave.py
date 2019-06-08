def interweave(str1, str2):
	string1 = ''.join(x + y for x, y in zip(str1, str2))
	string1 += (str1[len(str2):] if len(str1) > len(str2) else str2[len(str1):])
	print(string1)

interweave("Bhumika", "Vasusamarth")
