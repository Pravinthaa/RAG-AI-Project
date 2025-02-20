import pandas as pd

def load_travel_tips(csv_file):
    """Load travel tips from a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(csv_file)
        print("✅ CSV file loaded successfully!")
        print(df.head())  # Display first few rows
        return df
    except Exception as e:
        print(f"❌ Error loading CSV file: {e}")
        return None

# Example usage
if __name__ == "__main__":
    csv_file = "travel_tips.csv"  # Ensure this file exists
    df = load_travel_tips(csv_file)
