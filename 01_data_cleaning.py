import pandas as pd


# ==============================
# 1. Load the dataset
# ==============================

df = pd.read_csv("vgsales.csv")

# ==============================
# 2. Explore the data
# ==============================

print("Dataset Overview:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Description: ")
print(df.describe())

print("\nDataset Data Type: ")
print(df.dtypes)

# ==============================
# 3. Clean the data
# ==============================

df = df.drop_duplicates()

# ==============================
# Identifying missing data
# ==============================

print("\nIdentifying missing data: ")
print(df.isna().sum())

# ==============================
# Handling missing data
# ==============================

df["Critic_Score"] = df["Critic_Score"].fillna(df["Critic_Score"].median())

# ==============================
# Handling with corner cases
# ==============================

df["Global_Sales"] = (df["NA_Sales"] + df["EU_Sales"] + df["JP_Sales"] + df["Other_Sales"]).round(2)

# ==============================
# Export to a new file
# ==============================

df.to_csv("vgsales_cleaned.csv", index=False)