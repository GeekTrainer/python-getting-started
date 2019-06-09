int_charged = input('How much interest did you pay?')
print('\nYou entered Interest: ' + int_charged)

loan_amount = input('How much did you borrow? ')
print('\nYou entered loan amount: ' + loan_amount)

print('\nCalculateInterest')
int_rate = float(int_charged) / float(loan_amount) 
int_percent = float(int_rate)*100

print('\nshow result')
print('interest rate is ' + str(int_percent))