def get_all_lists(NewFile : str):
    list1 = []
    for line in open(NewFile, encoding = "utf8"):
        line = line.replace(', ', ' ')
        line = line.replace('? ', ' ')
        line = line.replace('. ', ' ')
        line = line.replace('! ', ' ')
        list1.append(line.replace(', ', ' ').split())
    print(list1)
    return list1

def get_all_words(list1):
    return list1

def make_key(word: str):
    return ''.join(word)

def build_frequency_list(NewFile: str):
    freqMappings = {}
    for line in get_all_lists(NewFile):
        for word in get_all_words(line):
            key = make_key(word)
            if key not in freqMappings:
                freqMappings[key] = 1
            else:
                freqMappings[key] += 1

    return extract_freqList(freqMappings)

def extract_freqList(freqGenerator_list: {str : [int]}):
    freqGenerator = sorted(freqGenerator_list[key])
    print (freqGenerator[-20: -1])  

build_frequency_list("WarAndPeace.txt")
