# BLAST OFF

user_input = int(input('Commence count down: '))

count = 0

while count <= user_input: 
  if user_input > 20:
    print('Count down sequence is TOO HIGH! Do not pass 20.')
    user_input = int(input('Commence count down: '))
  else:   
    print(user_input)
    user_input = user_input - 1
print('BLAST OFF!!')