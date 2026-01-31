import pandas as pd

# 1. Total orders placed by users with Gold membership
# We merge the dataframes on the common 'user_id' column
gold_orders_df = pd.merge(orders, users, on='user_id')
total_gold_orders = gold_orders_df[gold_orders_df['membership'] == 'Gold'].shape[0]

# 2. Number of distinct users who placed at least one order
# We use the unique() or nunique() function on the orders dataframe
distinct_users_count = orders['user_id'].nunique()

print(f"Total Gold Orders: {total_gold_orders}")
print(f"Distinct Ordering Users: {distinct_users_count}")