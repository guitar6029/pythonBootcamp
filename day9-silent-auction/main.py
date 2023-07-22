silent_auction_buyers = []
print('''
 $$$$$$\  $$\ $$\                      $$\            $$$$$$\                        $$\     $$\                     
$$  __$$\ \__|$$ |                     $$ |          $$  __$$\                       $$ |    \__|                    
$$ /  \__|$$\ $$ | $$$$$$\  $$$$$$$\ $$$$$$\         $$ /  $$ |$$\   $$\  $$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\  
\$$$$$$\  $$ |$$ |$$  __$$\ $$  __$$\\_$$  _|        $$$$$$$$ |$$ |  $$ |$$  _____|\_$$  _|  $$ |$$  __$$\ $$  __$$\ 
 \____$$\ $$ |$$ |$$$$$$$$ |$$ |  $$ | $$ |          $$  __$$ |$$ |  $$ |$$ /        $$ |    $$ |$$ /  $$ |$$ |  $$ |
$$\   $$ |$$ |$$ |$$   ____|$$ |  $$ | $$ |$$\       $$ |  $$ |$$ |  $$ |$$ |        $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$  |$$ |$$ |\$$$$$$$\ $$ |  $$ | \$$$$  |      $$ |  $$ |\$$$$$$  |\$$$$$$$\   \$$$$  |$$ |\$$$$$$  |$$ |  $$ |
 \______/ \__|\__| \_______|\__|  \__|  \____/       \__|  \__| \______/  \_______|   \____/ \__| \______/ \__|  \__|
                                                                                                                     
                                                                                                                    
    )_______(
    |"""""""|_.-._,.---------.,_.-._
    |       | | |               | | ''-.
    |       |_| |_             _| |_..-'
    |_______| '-' `'---------'` '-'
    )"""""""(
   /_________\
   `'-------'`
 .-------------.
/_______________\
''')

userName = input('\n\n\nWhat is your name? : ')
priceBid = int(input('Enter your bid : ex 120 : '))

person = {
  "name": userName,
  "priceBid": priceBid
}

#add person to the list of buyers
silent_auction_buyers.append(person)
moreBuyers = True

while moreBuyers:
  isMore = input('Are there more buyers ? "Y" for yes, "N" for no :')
  if isMore.lower() == 'y':
    userName = input('What is your name? : ')
    priceBid = int(input('Enter your bid : ex 120 : '))
    person = {
      "name": userName,
      "priceBid": priceBid
    }
    silent_auction_buyers.append(person)  
  else:
    moreBuyers = False

def getHighestBid(silent_bidders):
  winner = {}
  isHighest = 0
  for bidder in silent_bidders:
    if bidder["priceBid"] > isHighest:
      isHighest = bidder['priceBid']
      winner = bidder
    print(f'Bidder : {bidder["priceBid"]}')

  print(f'The highest bid : {isHighest}')
  return winner 

winner = getHighestBid(silent_auction_buyers)
print(f'The winning bid goes to {winner["name"]}, congratulations !')
