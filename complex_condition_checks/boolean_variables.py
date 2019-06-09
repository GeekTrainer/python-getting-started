# I check to see if the requirements for honour roll are met
# and set a Boolean variable to True or False to remember
gpa = .95
lowest_grade = .81

if gpa >= .85 and lowest_grade >= .70:
	honour_roll = True
else:
	honour_roll = False

# Somewhere later in your code if you need to check if students is 
# on honour roll, all I need to do is check the boolean variable
# I set earlier in my code
if honour_roll:
	print('Well done')
