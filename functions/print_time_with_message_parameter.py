import datetime

# Print the current time and task name
def print_time(task_name):
    print(task_name)
    print(datetime.datetime.now())
    print()

# print timestamps to see how long sections of code 
# take to run, tell me what task was completed
first_name = 'Susan'
print_time('first name assigned')

for x in range(0,10):
	print(x)
print_time('loop completed')
