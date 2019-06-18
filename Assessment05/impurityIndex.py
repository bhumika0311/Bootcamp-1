alphabets = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
frequency = [0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0 ,0 , 0 , 0 , 0 ,0 , 0, 0, 0, 0 ,0, 0]
vowels = ['A', 'E', 'I', 'O', 'U']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
def impurityIndexCalc (Sentence):
    impurityIndex = 0.0
    Sentence = Sentence.upper()
    for x in Sentence:
        i = 0
        while i < 27:
            if alphabets[i] == x:
                frequency[i] += 1
                    
            i += 1


    print(frequency)
        

    
    for x in Sentence:
        i = 0
        while i < 27:
            if alphabets[i] in vowels and frequency[i] == 2:
                impurityIndex += 0.5

            if alphabets[i] in consonants and frequency[i] == 2:
                impurityIndex += 0.7

            if frequency[i] > 2:
                impurityIndex += 1.0

            if frequency[i] > 3:
                impurityIndex += 3.0

            i += 1

    return impurityIndex

print(impurityIndexCalc("The quick brown fox jumps over the lazy dog"))
    
    
