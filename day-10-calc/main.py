import art

####### start calc program
def start_calc():
  
  userInputA = input('Enter a number: ')
  while not userInputA.isnumeric():
    userInputA = input('Enter a number please: ')
      
  userOperator = input('Enter an operator : + , -, *, /, : ')
  userInputB = input('Enter a number: ')
  while not userInputB.isnumeric():
    userInputB = input('Enter a number please: ')
  
  if userInputA == 0 and userOperator == '/':
    userInputA = int(input('Enter a number which is not a zero: '))
    while userInputA == 0:
      userInputA = int(input('Enter a number which is not a zero: '))
    myVal = divide_nums(userInputA, userInputB)
  
  if userOperator == '+':
    myVal = add_nums(int(userInputA), int(userInputB))
  if userOperator == '-':
    myVal = subtract_nums(int(userInputA), int(userInputB))
  if userOperator == '*':
    myVal = multiply_nums(int(userInputA), int(userInputB))
  
  print(f'{userInputA} {userOperator} {userInputB} : ')
  print(f'Answer : {myVal}')
  return myVal

def add_nums(a,b):
  return a + b

def subtract_nums(a,b):
  return a - b

def multiply_nums(a,b):
  return a * b

def divide_nums(a, b):
  if a == 0:
    print('Cannot divide 0')
    askAgain(a,b)
  return a / b

print(art.logo)

myVal = start_calc()
userContinue = True


####### while user wants to continue
while userContinue:
  userAnswer = input("Would you like to continue : yes or no : ")
  if userAnswer == 'no':
    userContinue = False
  else :
    userInputA = input('Enter a number: ')
    while not userInputA.isnumeric():
      userInputA = input('Enter a number please: ')
      
    userOperator = input('Enter an operator : + , -, *, /, : ')
    #### if first value is zero and operator is '/'
    if int(userInputA) == 0 and userOperator == '/':
      userInputA = input('Enter a number which is not a zero: ')
      while not userInputA.isnumeric and int(userInputA) == 0:
        userInputA = input('Enter a number which is not a zero: ')
      myVal = divide_nums(myVal, int(userInputA))

    ## if operator +
    if userOperator == '+':
      myVal = add_nums(myVal, int(userInputA))
    ## if operator -
    if userOperator == '-':
      myVal = subtract_nums(myVal, int(userInputA))
    ## if operator *
    if myVal == '*':
      myVal = multiply_nums(myVal, int(userInputA))
    print(f'Answer : {myVal}')

print(f'Answer : {myVal}')


