day = int(input('Day (0-6)? '))
try:
  if day >= 1 and day <=5:
    print('Go to work!')
  elif day == 0 or day == 6:
    print('Sleep in!')
except:
  print('Not a valid entry, please select from 0 - 6.')

