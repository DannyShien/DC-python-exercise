# Dictionary Exercise 

# EXERCISE 1: 
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
# printing Elizabeth's phone number
print('Phone number: ', phonebook_dict['Elizabeth'])

# adding a new entry to dicitonary
phonebook_dict['Kareem'] = '938-489-1234'

# deleteing Alice's entry
del phonebook_dict['Alice']

# changing 'Bob's number'
phonebook_dict['Bob'] = '968-345-2345'

# print all phone entries
print('Phonebook entries: ', phonebook_dict)

# EXERCISE 2: 
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# getting the email address of Ramit
print('Ramit\'s email: ', ramit['email'])

# for email in ramit['email']: 
#   print('Ramit\'s email addresss: ', ramit['email'])

# getting ramit's first interst
print('Ramit\'s first interest: ', ramit['interests'][0])

# getting jasmine's email address
print('Jasmin\'s email address: ', ramit['friends'][0]['email'])

# getting Jan second interest
print('Jan\'s second interest: ', ramit['friends'][1]['interests'][1])

# LETTER SUMMARY:
word = input('Type a word: ')
count = [0]
letter = []
for letter in range(word):
  if letter == word[count]:
    print(letter)

