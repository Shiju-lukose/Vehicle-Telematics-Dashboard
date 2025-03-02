# Import essential libraries
import pandas as pd  # For handling datasets
import numpy as np   # For numerical operations

# Load dataset (make sure the file name is correct)
df = pd.read_csv("Telematicsdata.csv")

# Show the first 5 rows
print("First 5 Rows:\n", df.head())

# Check dataset info
print("\nDataset Info:")
df.info()

# Summary statistics of numerical columns
print("\nSummary Statistics:\n", df.describe())

# Count missing values in each column
print("\nMissing Values Count:\n", df.isnull().sum())

# Count duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Drop rows where 'timeMili' is missing
df = df.dropna(subset=['timeMili'])

# 🔹 Step 1: Identify Problematic Timestamps (Hours ≥ 24)
invalid_timestamps = df[df['timestamp'].str.contains("24:|25:|26:|27:", na=False)]
print("\nInvalid timestamps found:\n", invalid_timestamps)

# 🔹 Step 2: Remove Invalid Timestamps
df = df[~df['timestamp'].str.contains("24:|25:|26:|27:", na=False)]

# 🔹 Step 3: Convert 'timestamp' to Proper Datetime Format
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# 🔹 Step 4: Check for Any Remaining Invalid (NaT) Timestamps
print("\nInvalid (NaT) timestamps after conversion:", df['timestamp'].isnull().sum())

# Remove rows with NaT timestamps
df = df.dropna(subset=['timestamp'])

# Separate numeric values and GPS data from "value" column
df['is_GPS'] = df['value'].str.contains(",", regex=False, na=False)
df['GPS_Coordinates'] = df['value'].where(df['is_GPS'], np.nan)
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# Fix for empty GPS rows: Replace NaN values with "No GPS Data"
df['GPS_Coordinates'].fillna("No GPS Data", inplace=True)

# Drop duplicate rows
df = df.drop_duplicates()

# Final check
print("\nFinal Dataset Info:")
df.info()

# Save the cleaned dataset
df.to_csv("Cleaned_Telematicsdata.csv", index=False)

print("\n✅ Data cleaning complete. Cleaned dataset saved as 'Cleaned_Telematicsdata.csv'.")
