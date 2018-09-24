# How many coins do you want?
coins = 0 
print('You have 0 coins.')
response = input('Do you want a coin? ')
response = response.lower()
# This works, but when entering anything but 'yes', its prompts the 'come again' message. 
while response == 'yes': 
  coins = coins + 1
  print('You now have %d coins' % (coins))
  response = input('Do you want a coin? ')
  response = response.lower()
print('Come again.')
  
# try:
#   while response == 'yes':
#     if response == 'yes': 
#       coins = coins + 1
#       print('You now have %d coins' % (coins))
#       response = input('Do you want a coin? ')
#       response = response.lower()
#     elif response == 'no':
#       print('Come again.')  
# except:
#   print('Yes or no buddy..move along.')
  
  
 
    
  
