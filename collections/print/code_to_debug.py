int_charged = input('How much interest did you pay?')

loan_amount = input('How much did you borrow? ')

int_rate = float(int_charged) / float(loan_amount) 

int_percent = float(int_rate)*100

print('interest rate is ' + str(int_percent))