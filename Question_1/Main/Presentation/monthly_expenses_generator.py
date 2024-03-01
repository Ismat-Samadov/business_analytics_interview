import random
import pandas as pd
from datetime import datetime

def generate_monthly_expenses():
    categories = {
        "restaurant": ["Fast Food", "Casual Dining", "Fine Dining"],
        "market": ["Groceries", "Fresh Produce", "Meat and Seafood", "Dairy", "Bakery", "Snacks", "Beverages", "Frozen Foods", "Canned Goods"],
        "gas_stations": ["Gasoline", "Snacks", "Beverages", "Automotive Supplies"],
        "transport": ["Public Transportation", "Taxi/Uber/Lyft", "Car Rental", "Vehicle Maintenance"]
    }

    locations = ["Baku", "Ganja", "Sumqayit", "Mingachevir", "Lankaran", "Shirvan", "Yevlakh", "Nakhchivan", "Shaki", "Gabala"]

    data = []
    for i in range(100):
        customer_id = i + 1
        birth_date = datetime(1980 + random.randint(0, 20), random.randint(1, 12), random.randint(1, 28)).strftime('%Y-%m-%d')
        location = random.choice(locations)
        for category, subcategories in categories.items():
            for subcategory in subcategories:
                transaction_date = datetime(2024, 1, random.randint(1, 31)).strftime('%Y-%m-%d')
                amount = round(random.uniform(10, 30), 2)
                data.append([customer_id, transaction_date, category, subcategory, amount, birth_date, location])

    df = pd.DataFrame(data, columns=['customer_id', 'transaction_date', 'category', 'subcategory', 'amount', 'birth_date', 'location'])

    return df

if __name__ == "__main__":
    df = generate_monthly_expenses()
    print(df)
