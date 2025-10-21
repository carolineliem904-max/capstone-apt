import pandas as pd

df = pd.read_csv("/Users/carolineliem/Downloads/data_daegu_apartment.csv")

# --- Clean TimeToSubway column ---
def convert_time_to_minutes(val):
    """Convert subway time string to numeric minutes."""
    val = str(val).strip().lower()
    if "no_subway" in val or "no_bus" in val:
        return 30  # treat as far away
    # Replace '~' with '-' for uniformity
    val = val.replace("~", "-").replace("min", "").replace(" ", "")
    # Extract first number range
    if "-" in val:
        start, end = val.split("-")
        try:
            return (float(start) + float(end)) / 2  # take midpoint
        except:
            return None
    else:
        # just number (e.g. "5")
        try:
            return float(val)
        except:
            return None

df["TimeToSubway_min"] = df["TimeToSubway"].apply(convert_time_to_minutes)


# 1. Create new feature: building age
df["Age"] = 2025 - df["YearBuilt"]

# 2. Convert area to square meters
df["Size_m2"] = df["Size(sqf)"] * 0.092903

# 3. Encode categorical features
df["HallwayType"] = df["HallwayType"].astype("category")
df["SubwayStation"] = df["SubwayStation"].astype("category")

# 4. Drop the original 'YearBuilt' and 'Size(sqf)' if redundant
df = df.drop(columns=["YearBuilt", "Size(sqf)"])

# 5. Check for missing values
print(df.isna().sum())

# 6. Quick statistical summary
print(df.describe())

df.to_csv("/Users/carolineliem/Documents/cleaned_daegu_apartment_v2.csv", index=False)
print("✅ Cleaned v2 dataset saved with numeric TimeToSubway_min column.")

# 0) Rows/cols unchanged except the intended swaps
print(df.shape, df.columns.tolist())

# 1) No NaNs (esp. in TimeToSubway_min)
print(df.isna().sum())

# If any NaNs show up in TimeToSubway_min, fill with median:
df["TimeToSubway_min"] = df["TimeToSubway_min"].fillna(df["TimeToSubway_min"].median())

# 2) Peek distribution of TimeToSubway_min
print(df["TimeToSubway_min"].describe())
print(sorted(df["TimeToSubway_min"].unique())[:10])  # first 10 unique values

# 3) Target still present
assert "SalePrice" in df.columns, "SalePrice missing!"
