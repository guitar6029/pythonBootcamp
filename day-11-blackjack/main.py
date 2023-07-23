import art
import random

userCards = []
dealerCards = []

def dealerPullsCard():
  dealerCards.append(getRandomCard())

def checkWhoWon():
  userScore = getScore(userCards)
  dealerScore = getScore(dealerCards)
  if userScore > dealerScore and userScore <= 21:
    print(f'You have won : {userScore}')
    print(f'The dealer cards : {dealerCards}')

  if userScore <= 21 and dealerScore > 21:
    print(f'You have won : {userScore}')
    print(f'The dealer cards : {dealerCards}')
      
  if dealerScore > userScore and dealerScore <= 21:
    print(f'The house wins : {dealerScore}')
    print(f'The dealer cards : {dealerCards}')
   
  if userScore > 21 and dealerScore <= 21:
    print(f'Your score : {userScore} \n')
    print(f'Bust, the house wins : {dealerScore}')
    print(f'The dealer cards : {dealerCards}')
   
  if userScore == dealerScore:
    print(f'It\'s a draw')
    print(f'The user cards : {userCards}')
    print(f'The dealer cards : {dealerCards}')
       

def drawCard():
  userCards.append(getRandomCard())

def hitOrStandDealer():
  answer = ['hit', 'stand']
  return answer[random.randint(0, len(answer) - 1)]

def hitOrStand():
  answer = input('Do you want to hit or stand : ')
  return answer

def getScore(cards):
  score = 0
  for card in cards:
    score = score + card
  return score  

def getRandomCard(): 
  return cards[random.randint(1, len(cards) - 1)]
  
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)

dealersTurn = False
usersTurn = True
userScore = 0
dealerScore = 0

bust = False

draw = False
quitGame = False

userWon = False
userLost = False
dealerWon = False
dealerLost = False
bustDealer = False

while not quitGame:
  #reset scores
  userScore = 0
  dealerScore = 0

  #rest cards
  userCards = []
  dealerCards = []
  
  #reset users turn to true
  usersTurn = True
  #get two cards for the user
  userCards.append(getRandomCard())
  userCards.append(getRandomCard())
  #get two cads fo the dealer
  dealerCards.append(getRandomCard())
  dealerCards.append(getRandomCard())

  userScore = getScore(userCards)
  dealerScore = getScore(dealerCards)

  #score 
  print(f'\nYou have : {userCards} : {userScore}')
  print('---------------------------------------')
  print(f'The dealer has : [{dealerCards[len(dealerCards) - 1]}, ? ] \n')
  
  userChoice = hitOrStand()

  while userChoice == 'hit':
    drawCard()
    userScore = getScore(userCards)
    print(f'You have : {userCards} : {userScore}')
    print('---------------------------------------')
    print(f'The dealer has : [{dealerCards[len(dealerCards) - 1]}, ? ]\n')
    if userScore > 21:
      print('Bust, better luck next time')
      bust = True
      userChoice = 'stand'
    else:
      userChoice = hitOrStand()
    
        
   
  
      
  if userChoice == 'stand' or bust:
    # dealer goes next
    dealerScore = getScore(dealerCards)
    while dealerScore <= 16 or not bustDealer:
      dealerCards.append(getRandomCard())
      print(f'Dealer cards {dealerCards}')
      dealerScore = getScore(dealerCards)
      print(f'Dealer score : {dealerScore}')
      if dealerScore >= 17 and dealerScore <= 21:
        dealerChoice = 'stand'
      if dealerScore >= 21:
        bustDealer = True
        
  
  #check who won
  checkWhoWon()
  answer = input('Do you want to continue playing ? : Yes or q to quit : ')
  if answer == 'q':
    quitGame = True
  
