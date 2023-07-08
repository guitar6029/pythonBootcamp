# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
myChoice = int(input("Chose : 0 for Rock, 1 for Paper, 2 for Scissors : "))
npcSelect = random.randint(0,2)
choice = ['Rock', 'Paper', 'Scissors']
print(f'npcSelect : {npcSelect}')
if myChoice == 0:
    print(f"You chose {choice[myChoice]} \n")    
    print("""
        _______
    ---'   ____)
            (_____)
            (_____)
            (____)
---.    __(___)
    """)
    if npcSelect == 1:    
        print(f'Npc chose {choice[npcSelect]} \n')
        print("""
        _______
    ---'    ____)______
                _______)
                _______)
                _______)
    ---._____________)
    """)
        print('You lose.')
    if npcSelect == 2:
        print(f'Npc chose {choice[npcSelect]} \n')
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print('You win.')
    else:
        print(f'Npc chose {choice[npcSelect]} \n')
        print("""
        _______
    ---'   ____)
            (_____)
            (_____)
            (____)
---.    __(___)
    """)
    print('Its a tie.')

if myChoice == 1:
    print(f"You chose {choice[myChoice]} \n")
    print("""
        _______
    ---'    ____)______
                _______)
                _______)
                _______)
    ---._____________)
    """)
    if npcSelect == 0:
        print(f'Npc chose {choice[npcSelect]} \n')
        print("""
        _______
    ---'   ____)
            (_____)
            (_____)
            (____)
---.    __(___)
    """)
        print('You win.')
    if npcSelect == 1:
        print(f'Npc chose {choice[npcSelect]} \n')
        print("""
        _______
    ---'    ____)______
                _______)
                _______)
                _______)
    ---._____________)
    """)
        print('Its a tie.')
    else:
        print(f'Npc chose {choice[npcSelect]} \n')
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")    
        print('You lose.')

if myChoice == 2:
    print(f"You chose {choice[myChoice]} \n")    
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    if npcSelect == 0:
        print(f'Npc chose {choice[npcSelect]} \n')
        print("""
        _______
    ---'   ____)
            (_____)
            (_____)
            (____)
---.    __(___)
    """)
        print('You lose.')
    if npcSelect == 1:
        print(f'Npc chose {choice[npcSelect]} \n')
        print("""
        _______
    ---'    ____)______
                _______)
                _______)
                _______)
    ---._____________)
    """)
        print('You win')        
    else:
        print(f'Npc chose {choice[npcSelect]} \n')
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")    
        print('its a tie.')
