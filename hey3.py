print('Please fill in the blanks below:')
print('__(name)__ is pleased to understand this much in __(subject)__!')
name = input('What is your name? ')
name = name.capitalize()
subject = input('What is the subject? ')
subject = subject.capitalize()

print('%s is pleased to understand this much in %s!' % (name, subject))
