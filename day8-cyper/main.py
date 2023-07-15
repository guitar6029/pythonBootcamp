alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
userQuit = False

    
def caesar(text, shiftVal, direction):
  if direction == 'encode':
    encryptedMsg = ''
    for letter in text:
      position = alphabet.index(letter)
      shiftedPosition = position + shiftVal
      if shiftedPosition > 26:
        new_position = shiftedPosition % 26
        new_positionValue = alphabet[new_position]
        encryptedMsg += str(new_positionValue)
      else:
        encryptedMsg += alphabet[shiftedPosition]
    return encryptedMsg
  elif direction == 'decode':
    decryptedMsg = ''
    for letter in text:
      position = alphabet.index(letter)
      shiftedPosition = position - shiftVal
      if shiftedPosition < 0:
        new_position = shiftedPosition % 26
        new_positionValue = alphabet[new_position]
        decryptedMsg += str(new_positionValue)
      else:
        decryptedMsg += alphabet[shiftedPosition]
    return decryptedMsg
  elif direction == 'q':
    userQuit = True
    return 'q'
  else:
    return False



while not userQuit:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt , or q to quit :\n")
  if direction == 'q':
    userQuit = True
  else:
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    letters = []
    
    for letter in text:
      letters.append(letter)
      
    answer = caesar(text, shift, direction)
    if answer == 'q':
      userQuit = True
    elif answer == False:
      print("Please enter encode , decode or q to quit \n")
    else:
      if direction == 'encode':
        print(f'Your encrypted message is {answer}')
      else:
        print(f'Your decrypted message is {answer}')
  
