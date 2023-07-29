
import art 
guessed = False
def getNumberOfTries(tries):
  if tries == 1:
    return 10
  else:
    return 5

print(art.logo)
number = 15
count = 1
difficulty = int(input('Enter the level of difficulty : 1 for easy, 2 for hard : '))
numberOfTries = getNumberOfTries(difficulty)

while count <= numberOfTries:
  print(f'Number of tries : {numberOfTries}')
  guessedNumber = int(input('Guess the number between 1 and 100 : '))
  print(f'Guessed Number : {guessedNumber}')
  if guessedNumber == number:
    print("Correct!")
    guessed = True
    break
  else:
    print('Try again\n')
    if guessedNumber < number:
      print('Too Low')
    else:
      print('Too High')
    count = count + 1  

if not guessed:
  print("Out of tries! The correct number was:", number)
  
    
