# Reflection
# 1. What surprised me most about Python lists was how simple they are to
# use and modify. I learned that there are many ways to organize information,
# including adding, deleting, sorting, and finding specific items.
#
# 2. Python lists could have helped me when completing assignments that
# involved a lot of numbers. Instead of calculating everything by hand
# or using Excel, I could use lists to store the numbers and quickly
# calculate the sum, average, maximum, and minimum.


# Exercise 1

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# Exercise 2

print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])


# Exercise 3

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because they cannot be changed.")

print(coords)


# Exercise 6

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print(prices)
print(discounted)


# Exercise 8

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))

average = sum(high_sales) / len(high_sales)
print("Average:", average)