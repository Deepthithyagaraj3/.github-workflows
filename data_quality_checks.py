import pandas as pd

# Load the dataset
df = pd.read_csv("data.csv")

# Define validation rules
def validate_data(df):
    errors = []

    # Check for missing values
    if df.isnull().sum().sum() > 0:
        errors.append("❌ Error: Missing values detected in the dataset.")

    # Check for negative salaries
    if (df["salary"] < 0).any():
        errors.append("❌ Error: Negative salary values found!")

    if errors:
        for error in errors:
            print(error)
        raise ValueError("❌ Data Quality Check Failed. Fix errors before proceeding.")
    else:
        print("✅ Data Quality Passed. Ready for database upload.")

# Run validation
validate_data(df)
