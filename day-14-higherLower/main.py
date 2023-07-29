import random 
import art
import game_data

gameOver = False
print(art.logo)
def getRandomPerson():
  randomNum = random.randint(0, len(game_data.data) - 1)
  return game_data.data[randomNum]

personA = getRandomPerson()

while not gameOver:
  
  print(f'{personA["name"]} , a {personA["description"]} from {personA["country"]} , has {personA["follower_count"]} followers')
  print(art.vs)

  personB = getRandomPerson()
  while personA["name"] == personB["name"]:
    personB = getRandomPerson()

  print(f'{personB["name"]} , a {personB["description"]} from {personB["country"]} , has lower or higher follower count ?')

  userInput = input('Do you think this number is higher or lower ? Enter higher or lower : ') 
  #if lower
  if personA["follower_count"] < personB["follower_count"]:
    if userInput == 'higher':
      print('Nope, you lose! Better luck next time.')
      gameOver = True
    else:
      personA = personB
      personB = getRandomPerson()
      while personA["name"] == personB["name"]:
       personB = getRandomPerson()
  #if higher
  else:
    if userInput == 'lower':
      personA = personB
      personB = getRandomPerson()
      while personA["name"] == personB["name"]:
       personB = getRandomPerson()
    else:
      print('Nope, you lose! Better luck next time.')
      gameOver = True
  
