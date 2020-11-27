hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
#Iterate through the prices list and add each price to the variable total_price.
for price in prices:
  total_price += price
#After your loop, create a variable called average_price that is the total_price divided by the number of prices.
average_price = total_price / len(prices)
#Print the value of average_price so the output looks like:
print('Average Haircut Price ' + str(average_price))
#Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.
new_prices = [price - 5 for price in prices]
print(new_prices)

#Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(total_revenue)
#Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.
average_daily_revenue = total_revenue/7
print(average_daily_revenue)
#Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]<30]
print(cuts_under_30)