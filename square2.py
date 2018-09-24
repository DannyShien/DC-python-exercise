# Print NxN square of *. How many sqaures?
squares = int(input('How big is the square? '))

count_row = 0

while count_row <= squares:
  count_col = 0
  while count_col <= squares: 
    print('*', end = '')
    count_col = count_col + 1
  count_row = count_row + 1
  print()  