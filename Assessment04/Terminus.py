DirectionsUpDown = ["N", "S"]
Movements = [1, -1]
DirectionsLeftRight = ["E", "W"]
pathsLeftRight = dict(zip(DirectionsLeftRight, Movements))
pathsUpDown = dict(zip(DirectionsUpDown, Movements))

def Terminus (latticePoint, listOfStrings):
    i = 0
    x = latticePoint[0]
    y = latticePoint[1]
    while i < len(listOfStrings):
        if [listOfStrings[i][-1]] in DirectionsUpDown:
            x += pathsUpDown[listOfStrings[i][-1]]
            y += pathsUpDown[listOfStrings[i][-1]]
        else:
            x += pathsLeftRight[listOfStrings[i][-1]]
            y += pathsLeftRight[listOfStrings[i][-1]]
            
        i += 1
    finalPoint = "(" + x + "," + y + ")"
    
print(Terminus((1, 1), ["1N", "3NW"]))
