# This function will take a name and return the 
# first letter of the name
def get_initial(name):
    initial = name[0:1].upper()
    return initial

#Ask for someone's name and return the initials
first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

print('Your initial is: ' + first_name_initial)