# Print a box
width = int(input('Width?: '))
height = int(input('Height?: '))

rows = 0
cols = 0

while cols < width:
  while rows < height:
    if rows == 0 or rows == (height - 1):
      print('* ', end='')
    elif cols > 0 and cols < width-1:
      print('  ', end='')
    else:
      print('* ', end='')
    rows = rows + 1
  cols = cols + 1
  rows = 0
  print()






