# 2 uppercase letters from A to Z,
# 2 lowercase letters from a to z,
# 2 digits from 0 to 9,
# 2 punctuation signs such as !, ?, “, # etc.

import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
#....
digit1=chr(random.randint(48,57)) #Generate a random digit(based on ASCII code)
digit2=chr(random.randint(48,57)) #Generate a random digit(based on ASCII code)
#....
punctuation1=chr(random.randint(32,152)) #Generate a random punctuation
punctuation2=chr(random.randint(32,152)) #Generate a random punctuation

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuation1 + punctuation2
password = shuffle(password)

#Ouput
print(password)