initial_amount = float(input('How much money are you initially putting in the account? '))
interest_rate = float(input('What is the percent interest rate? '))
year = int(input('How many years? '))

total = round(initial_amount*(1+(interest_rate/100))**year,2) #round to the second decimal place

print('After ' + str(year)  + ' years, you will have: ' + '$' + str(total))
