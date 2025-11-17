import pandas as pd
from pathlib import Path

class DataExplorer:
    def __init__(self, data_folder="./data/raw"):
        self.data_folder = Path(data_folder)

    def explore_file(self, filename, display_samples=3):
        try:
            file_path = self.data_folder / filename
            df = pd.read_excel(file_path)

            print(f"Shape: {df.shape} (rows: {df.shape[0]}, columns: {df.shape[1]})")

            print(f"Columns ({len(df.columns)}):")
            for i, col in enumerate(df.columns, 1):
                print(f"   {i:2d}. {col}")

            print(f"\nData Types:")
            print(df.dtypes)

            print(f"\nFirst {display_samples} sample rows:")
            for i in range(min(display_samples, len(df))):
                print(f"\n--- Row {i+1} ---")
                for col in df.columns[:5]:
                    value = df.iloc[i][col]
                    if isinstance(value, str) and len(value) > 50:
                        value = value[:50] + "..."
                    print(f"   {col}: {value}")
                if len(df.columns) > 5:
                    print(f"   ... and {len(df.columns) - 5} more columns")

            print(f"\nMissing values overview:")
            missing_count = df.isnull().sum()
            if missing_count.sum() > 0:
                for col, count in missing_count.items():
                    if count > 0:
                        percentage = (count / len(df)) * 100
                        print(f"   {col}: {count} missing ({percentage:.1f}%)")
            else:
                print("   No missing values found")

            return df
        
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            return None

def main():
    explorer = DataExplorer()

    files_to_explore = [
        "Occupation Data.xlsx",
        "Skills.xlsx", 
        "Interests.xlsx",
        "Knowledge.xlsx",
        "Work Values.xlsx",
        "Education, Training, and Experience.xlsx",
        "Abilities.xlsx",
        "Task Statements.xlsx",
        "Technology Skills.xlsx"
    ]

    all_dataframes = {}

    for filename in files_to_explore:
        df = explorer.explore_file(filename)
        if df is not None:
            all_dataframes[filename] = df
        
        input(f"\nPress Enter to continue to next file...")

    print(f"Explored {len(all_dataframes)} files successfully")
    return all_dataframes

if __name__ == "__main__":
    all_dataframes = main()