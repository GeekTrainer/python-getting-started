# This function will take a name and return the 
# first letter of the name
# Parameters
    # name: is the name of the person
    # force_uppercase: indicates if you always want the initial to be in upppercase
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

#Ask for someone's name and return the initial
first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False)

print('Your initial is: ' + first_name_initial)