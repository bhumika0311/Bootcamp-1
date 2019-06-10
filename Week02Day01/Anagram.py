alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mapping1 = dict(zip(alphabets, occurrences))
mapping2 = dict(zip(alphabets, occurrences))

def isAnagram (string1, string2):

  string1 = string1.replace(' ', '')
  string2 = string2.replace(' ', '')

  n = 0
  while n < len(string1):
    mapping1[string1.upper()[n]] += 1
    n += 1

  m = 0
  while m < len(string2):
    mapping2[string2.upper()[m]] += 1
    m += 1

  return mapping1 == mapping2

print(isAnagram('Abc', 'Bc a'))