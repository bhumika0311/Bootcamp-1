def rle(inputString):
  ans = ""
  count = 1
  i = 0

  for i in len(inputString):
    if inputString[i] == inputString[i + 1]: 
		  count += 1

    else:
        if count == 1:
            ans = ans + inputString[i]
      
        else:
            ans = ans + inputString[i] + count      
			
        count = 1			
        
    if count != 1:
        ans = ans + count
	
	return ans if len(ans) < len(inputString) else inputString

print(rle("aaabcdsssseddd"))
