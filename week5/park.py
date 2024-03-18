# Write program to simulate a ticketing system in an amusement park. 
# Get input for a party with user’s name and birthday(date, month, year). 
# Calculate price based on age (kids , senior cotizen : 50rs, adults : 75). 
# On Tuesdays and Thursdays give 20% discount on total cost of tickets. 
# Use relevant dateTime modules in python

'''name, birthday 
age cacluate
dictionary {} - category prize
discount
'''
import calendar
from datetime import datetime

def calculateToday():
    today = datetime.today()
    presentYear = today.year
    presentDay = calendar.day_name[today.weekday()]
    return presentYear, presentDay

def calculateAge():                             #calculate age for each member 
    for customerName in customerNames.values() :
       birthYear = int(customerName[-4:])
       ageList.append(presentYear - birthYear)
    
def price():                                 # defining function for calculate prize                
    totalPrice = 0
    for age in ageList:
        if age > 14 and age < 60:
            totalPrice += 75
        elif age <= 14 or age >= 60:
            totalPrice += 50
    return totalPrice

def applyDiscount(amount):
    amount = amount - (0.2 * amount)
    return amount

customerNames = {}
ageList = []
discountDates = ['Monday', 'Thursday']

count = int(input("How many members? "))
for i in range(count):
    name = input("Enter your name: ") 
    birthday = input("Enter your Birthday (date-month-year): ")
    customerNames[name] = birthday

presentYear, presentDay = calculateToday()
calculateAge()
ticketAmount = price()
if presentDay in discountDates:
    ticketAmount = applyDiscount(ticketAmount)
print("Your total amount: ", ticketAmount)