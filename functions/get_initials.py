# This function will return the first initial of a name
def get_initial(name):
	initial = name[0:1].upper()
	return initial

# Ask for someones name and return the initials
first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

middle_name = input('Enter your middle name: ')
middle_name_initial = get_initial(middle_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial \
	+ middle_name_initial + last_name_initial)

