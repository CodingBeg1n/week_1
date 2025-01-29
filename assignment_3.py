##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''

year1 = int(input('Please input the first year:'))
year2= int(input('Please input the second year:'))

difference = (year2 - year1)

print('Year1',year1)
print('Year2',year2)
print('Difference', difference)

#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''
# I am so unsure if this is right, I had to look up stuff outside the site
def fahrenheit_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
fahrenheit = float(input('Please input Fahrenheit:'))

celsius = fahrenheit_to_celsius(fahrenheit)

print(f"Fahrenheit:{fahrenheit:.0f}")
print(f"Celsius: {celsius:.2f}")
#%%
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''

def usd_to_euro(usd_amount):
    exchange_rate = 0.97
    euro_amount = usd_amount * exchange_rate
    return euro_amount

usd_input = int(input('Eneter the amount of US Dolalrs:'))

euro_output = usd_to_euro(usd_input)

print(usd_input)
print(euro_output)


##### ASSIGNMENT ENDS HERE #####
