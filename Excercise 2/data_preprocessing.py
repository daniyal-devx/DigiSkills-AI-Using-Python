import pandas as pd

# --- Task 1: Dataset Loading ---
print("--- TASK 1: Dataset Loading ---")
df = pd.read_csv('HousePricePrediction.csv')
print("First 10 rows:")
print(df.head(10))
print("\n" + "="*50 + "\n")

# --- Task 2: Data Exploration ---
print("--- TASK 2: Data Exploration ---")
print("Shape of the dataset:", df.shape)
print("\nData Types:\n", df.dtypes.head()) # Showing top 5 for brevity
print("\nSummary Statistics of numerical features:\n", df.describe())
print("\n" + "="*50 + "\n")

# --- Task 3: Data Cleaning ---
print("--- TASK 3: Data Cleaning ---")
print("Total missing values before cleaning:", df.isnull().sum().sum())

# Dropping rows without a target price
df = df.dropna(subset=['SalePrice'])

# Filling missing numerical values with the median
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col] = df[col].fillna(df[col].median())

# Filling missing categorical values with the mode
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("Total missing values after cleaning:", df.isnull().sum().sum())

# Checking and removing duplicates
print("Duplicates found:", df.duplicated().sum())
df = df.drop_duplicates()
print("\n" + "="*50 + "\n")

# --- Task 4: Feature Selection ---
print("--- TASK 4: Feature Selection ---")
# Removing the 'Id' column as it has no predictive power
df = df.drop('Id', axis=1)
print("Removed 'Id' column. Remaining columns shape:", df.shape)
print("\n" + "="*50 + "\n")

# --- Task 5: Data Preprocessing ---
print("--- TASK 5: Data Preprocessing ---")
# Converting categorical text variables into numerical form (One-Hot Encoding)
df_encoded = pd.get_dummies(df, drop_first=True)

print("Preview of the final preprocessed dataset ready for Machine Learning:")
print(df_encoded.head())

# Saving the cleaned dataset for future use
df_encoded.to_csv('cleaned_dataset.csv', index=False)