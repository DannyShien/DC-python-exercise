# Upppercase a string.
string = 'This is the string exercise.'
print('Uppercase: ', string.upper())

#Capitalizing a string. 
print('Capitalize: ', string.capitalize())

#Reversing a string. 
print('Reverse: ',string[::-1])

#Leetspeak.
word = str(input('Type a word or phrase: '))
response = word.lower()
count = 0
while count < len(word): 
  if word[count] == 'a':
    print(4, end = '')
  elif word[count] == 'e': 
    print(3, end = '')
  elif word[count] == 'g':
    print(6, end = '')
  elif word[count] == 'i':
    print(1, end = '')
  elif word[count] == 'o':
    print(0, end = '')
  elif word[count] == 's': 
    print(5, end = '')
  elif word[count] == 't':
    print(7, end = '')
  else: 
    print(word[count], end = '')
  count += 1
print()

#Long-long Vowels
response = input('Type a word or phrase: ')
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0 
while count < len(response):
  if response[count] == vowels[0]:
    print(response[count] * 5, end = '')
  elif response[count] == vowels[1]: 
    print(response[count] * 5, end = '')
  elif response[count] == vowels[2]: 
    print(response[count] * 5, end = '')
  elif response[count] == vowels[3]: 
    print(response[count] * 5, end = '')
  elif response[count] == vowels[4]: 
    print (response[count] * 5, end = '')
  else:
    print(response[count], end = '')
  count += 1    
print()

