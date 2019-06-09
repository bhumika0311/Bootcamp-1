monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

numberOfDaysInEveryMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

monthNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

##########################################################################

def isLeapYear(year):
  year = (int)(year)
  return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

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

  numberOfDays = str(numberOfDays)
  endNumber = date[2] + numberOfDays

  while (len(endNumber) < 7):
    endNumber = endNumber[:4] + str(0) + endNumber[4:]

  print(endNumber)

#############################################################################

DateToNumber("7 Mar,2020")

