import os
import pandas as pd
import requests

# We query meals starting with letters: b, c, p, s (Beef/Burger, Chicken, Pizza/Pasta, Seafood/Salad)
LETTERS = ["b", "c", "p", "s"]
BASE_URL = "https://www.themealdb.com/api/json/v1/1/search.php"

all_meals = []

for letter in LETTERS:
    response = requests.get(BASE_URL, params={"f": letter})
    meals = response.json().get("meals")
    if meals:
        all_meals.extend(meals)
        print(f"Fetched meals starting with '{letter}': {len(meals)} items")

# Put into a clean table with only the columns we care about
df = pd.DataFrame(all_meals)
columns = {
    "idMeal": "item_id",
    "strMeal": "item_name",
    "strCategory": "category",
    "strArea": "cuisine",
}
df = df[list(columns.keys())].rename(columns=columns)

# Save inside data/seed folder relative to project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(PROJECT_ROOT, "data", "seed", "food_menu.csv")
os.makedirs(os.path.dirname(file_path), exist_ok=True)
df.to_csv(file_path, index=False)

print(f"\nSUCCESS! Saved {len(df)} menu items to:\n{file_path}")
print(df.head(10))