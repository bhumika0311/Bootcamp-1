def isAnagram(string1, string2):
  string1 = sorted(string1.replace(' ', '').upper())
  print(string1)
  string2 = sorted(string2.replace(' ', '').upper())
  return string1 == string2

print(isAnagram('Abc', 'CB A'))
