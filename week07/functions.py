# --- Self Assessment Questions ---
#1. The first bug I noticed was that the total wasn't adding correctly. I found it by reading the code and seeing that it was replacing the total instead of adding to it. This showed me that I can find mistakes by looking closely at my code.
#2. The function calculates the price after a discount. It takes the original price and membership tier. Gold gets 15% off, silver gets 10% off, and bronze gets 5% off. It returns the new price. Someone could understand how to use it without reading the code.
#3. I used ChatGPT to help understand errors and fix my code. 


# --- Exercise 1 ---

# Define calculation tax function 

def calculate_tax(price, rate): 
    return price * rate 

# Calling the function 

tax1 = calculate_tax(100, 0.07) 
tax2 = calculate_tax(250, 0.08) 

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50  

# --- Exercise 2 --- 
def apply_discount(price, tier): 
    if tier== "gold": 
        return price * 0.85 
    elif tier == "silver": 
        return price * 0.90 
    elif tier == "bronze": 
        return price * 0.95 
    else: 
        return price


    # Calling the function 

    price = 20 
    tiers = "gold", "silver", "bronze", "none"
             
for tiers in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")  

# --- Exercise 3 ---

# Write it out manually first, then refactor into a function 

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax 
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")  

# Refracted 
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final Price: ${final_price(200, 'gold', 0.07):.2f}") 


# --- Exercise 4 --- 
orders = [(200, "gold" ), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders: 
    total = final_price(price, tier, 0.07) 
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")


#--- Exercise 5 ---

# broken_sales.py - Debugged version

sales = [120, 80, 250, 90]

total = 0
for sale in sales:
    # Add each sale to the total instead of replacing it
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    # Move the counter inside the loop to count every sale
    count += 1
print(f"Count: {count}")

i = 0
# Use < instead of <= to avoid going outside the list
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---

x = 100 

def double_it(): 
    x = 999
    return x * 2

print(x) 
print(double_it())
print(x)
