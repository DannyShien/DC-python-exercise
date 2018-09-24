# Print multiplication table from 1 up to 10.

a = 1

while a <= 10: 
  b = 1
  # why is 'b' variable etablished before the nested loop?
  while b <= 10: 
    product = a * b
    print(a, ' * ', b, ' = ', product)
    b = b + 1
  print('\n')
  a = a + 1