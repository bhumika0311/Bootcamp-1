DirectionsUpDown = ["N", "S"]
Movements = [1, -1]
DirectionsLeftRight = ["E", "W"]
pathsLeftRight = dict(zip(DirectionsLeftRight, Movements))
pathsUpDown = dict(zip(DirectionsUpDown, Movements))
print(pathsLeftRight)
print(pathsUpDown)
def Terminus (latticePoint, listOfStrings):
    i = 0
    x = latticePoint[0]
    y = latticePoint[1]
    while i < len(listOfStrings):
        if [listOfStrings[i][-1]] in DirectionsLeftRight:
            x += pathsLeftRight.get([listOfStrings[i][-1]])
            
        elif [listOfStrings[i][-1]] in DirectionsUpDown:
            y += pathsUpDown.get([listOfStrings[i][-1]])
            
        elif [listOfStrings[i][-2]] in DirectionsLeftRight:
            x += pathsLeftRight.get([listOfStrings[i][-2]])
            
        elif [listOfStrings[i][-2]] in DirectionsUpDown:
            y += pathsUpDown.get([listOfStrings[i][-2]])
            
        i += 1
    return (x, y)
    
print(Terminus((1, 1), ["1N", "3NW"]))
