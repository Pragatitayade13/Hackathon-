import pandas as pd

# Load and prepare data
df = pd.read_csv('final_food_delivery_dataset.csv')
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

# 1 & 2. Basic Counts
total_gold_orders = df[df['membership'] == 'Gold'].shape[0]
distinct_users = df['user_id'].nunique()

# 3. Revenue by Membership + Cuisine
# Mapping specific styles to broader cuisine categories
def map_cuisine(name):
    name = name.lower()
    if any(word in name for word in ['punjabi', 'indian']): return 'Indian'
    if 'chinese' in name: return 'Chinese'
    if 'italian' in name: return 'Italian'
    return 'Other'

df['derived_cuisine'] = df['restaurant_name_x'].apply(map_cuisine)
rev_combo = df.groupby(['membership', 'derived_cuisine'])['total_amount'].sum().idxmax()

# 4. Highest Revenue Quarter
best_q = df.groupby(df['order_date'].dt.quarter)['total_amount'].sum().idxmax()

print(f"Gold Orders: {total_gold_orders}")
print(f"Unique Users: {distinct_users}")
print(f"Best Combo: {rev_combo}")
print(f"Best Quarter: Q{best_q}")