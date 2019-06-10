def isAnagram(string1, string2):
  string1 = sorted(string1.replace(' ', '').upper())
  string2 = sorted(string2.replace(' ', '').upper())
  return string1 == string2

def allAnagrams (string1):
    for line in open("words.txt", "r"):
        if isAnagram(string1, line[:len(string1)]) and len(line) == len(string1) + 1:
            print(line[:len(string1)])

allAnagrams("Listen")
