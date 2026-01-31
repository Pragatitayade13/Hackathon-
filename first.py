import pandas as pd

# Load the dataset
df = pd.read_csv('final_food_delivery_dataset.csv')

# 1. Total revenue (rounded to nearest integer) generated from orders placed in Hyderabad city
hyderabad_revenue = round(df[df['city'] == 'Hyderabad']['total_amount'].sum())
print(f"Total revenue in Hyderabad: {int(hyderabad_revenue)}")

# 2. Average order value (rounded to 2 decimals) for Gold members
gold_avg_value = df[df['membership'] == 'Gold']['total_amount'].mean()
print(f"Average order value for Gold members: {round(gold_avg_value, 2)}")

# 3. How many orders were placed for restaurants with rating ≥ 4.5?
high_rating_orders = len(df[df['rating'] >= 4.5])
print(f"Number of orders with restaurant rating >= 4.5: {high_rating_orders}")

# 4. How many orders were placed in the top revenue city among Gold members only?

gold_members_df = df[df['membership'] == 'Gold']

# Find the city with the highest total revenue among Gold members
top_gold_city = gold_members_df.groupby('city')['total_amount'].sum().idxmax()

# Count the number of orders in that specific city for Gold members
top_gold_city_orders = len(gold_members_df[gold_members_df['city'] == top_gold_city])
print(f"Orders in the top revenue city ({top_gold_city}) for Gold members: {top_gold_city_orders}")