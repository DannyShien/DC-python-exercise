import time
# 99 BOTTLES OF BEER ON THE WALL
bottles = 99

while bottles >= 0:
  if bottles == 0: 
    break
  print('%d bottles of beer on the wall, %d bottles of beer. Take one down, pass it around, %d bottles of beer on the wall' % (bottles, bottles, (bottles - 1)))
  bottles -= 1
  time.sleep(.2)


