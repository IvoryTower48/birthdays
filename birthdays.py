'''
This module will return the birthday of some renown people, in the format mm/dd/yyyy.
The database is handwritten, hence this module is quite limited in its utiity.
'''

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
''' This simple functions shows the keys of the birthdays dictionary, aka name and surname of the people in there. '''
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
''' This function will output the birthday related to the person given in input if in the dictionary, or a message error otherwise. '''
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

