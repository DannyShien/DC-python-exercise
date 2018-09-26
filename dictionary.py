# Dictionary Exercise 
#EXERCISE 1: 
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
# option 1
print('Phonebook entries: ', phonebook_dict)
# option 2
for person in phonebook_dict: 
  print('%s: %s' %(person, phonebook_dict[person]))
# for person, phone in phonebook_dict.items(): 
# print('%s: %s'(person, phone_dict))

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
print('Ramit\'s email address: ', ramit['email'])

# getting ramit's first interst
print('Ramit\'s first interest: ', ramit['interests'][0])

# getting jasmine's email address
#print('Jasmin\'s email address: ', ramit['friends'][0]['email'])
for f in ramit['friends']: 
  if f['name'] == 'Jasmine':
    print('Jasmine\'s email:', f['email'])

# getting Jan second interest
#print('Jan\'s second interest: ', ramit['friends'][1]['interests'][1])
for f in ramit['friends']: 
  if f['name'] == 'Jan':
    print('Jan\'s interest:', f['interests'][1])

# LETTER SUMMARY:
word_input = input('Type a word: ')
histogram = {}
list = []
counter = []

for i in word_input:
  if i not in list:
    list.append(i)
for i in list:
  counter.append(word_input.count(i))
for i in range(len(list)): 
  histogram[list[i]] = counter[i]
print(histogram)  
# ANOTHER EXAMPLE OF LETTER SUMMARY
# for letter in word_input: 
#   if letter in histogram: 
#     histogram[letter] += 1
#   else: 
#     histogram[letter] += 1

# WORD SUMMARY
sentence = str.split((input('Type a sentence: ')))
histogram = {}
word = []
tally = []

for i in sentence:
  if i not in word:
    word.append(i)
for i in word:
  tally.append(sentence.count(i))
for i in range(len(word)): 
  histogram[word[i]] = tally[i]
print(histogram) 



