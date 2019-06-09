# A student makes honour roll if their average is >=85
# and their lowest grade is not below 75
gpa = .95
lowest_grade = .6

# Option 1 I can check if both requirements are met
# by nesting two if statements
if gpa >= .85:
	if lowest_grade >= .70:
		print('Well done')

# Option 2 I can check if both requirements are met
# by using the AND operator
if gpa >= .85 and lowest_grade >= .70:
	print('Well done')
