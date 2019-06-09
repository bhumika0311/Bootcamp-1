monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

numberOfDaysInEveryMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

monthNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

##########################################################################

def isLeapYear(year):
  year = (int)(year)
  return (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0)

#########################################################################

def DateToNumber(date):
  date = (date.replace(' ', ',').split(','))
  numberOfDays = 0
  currentMonth = dict(zip(monthNames, monthNumber))[date[1]]

  for (x, y) in zip(monthNumber, numberOfDaysInEveryMonth):
     if x < currentMonth:
       numberOfDays += y

  numberOfDays += (int)(date[0])

  if isLeapYear(date[2]) and currentMonth > 2:
    numberOfDays += 1

  numberOfDays =  str(numberOfDays)

  currentYear = date[2]

  if len(numberOfDays) == 2:
      print(currentYear + '0' + numberOfDays)
  elif len(numberOfDays) == 1:
    print(currentYear + '00' + numberOfDays)
  else:
    print(currentYear + numberOfDays)
    

#############################################################################


DateToNumber("7 Jul,2020")

