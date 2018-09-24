for i in range(1, 101):
  
  if i % 3 == 0 and i % 5 == 0: 
    print('%d: FIZZBUZZ' % i)
  elif i % 3 == 0:
    print('%d: FIZZ' % i)
  elif i % 5 == 0: 
    print('%d: BUZZ' % i)
  else: 
    print(i)