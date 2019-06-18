alphabets = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0 ,0 , 0 , 0 , 0 ,0 , 0, 0, 0, 0 ,0, 0]
                           
def isPangram(Sentence):
    Sentence = Sentence.upper()
    for x in Sentence:
        i = 0
        while i < 27:
            if alphabets[i] == x:
                frequency[i] += 1
            i += 1

    print(frequency)

    for x in frequency:
        
        if x == 0:
            return False
        
    return True

print(isPangram("The quick brown x jumps over the lazy dog"))
    
