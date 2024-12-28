import os
import pandas as pd
import re

from persian_text_preprocessor import PersianTextPreprocessor
from english_text_preprocessor import EnglishTextPreprocessor

# Path to the zipped file
english_file_path = "DataSource/mizan/mizan_en.txt"
persian_file_path = "DataSource/mizan/mizan_fa.txt"
output_directory = "DataSource"


def load_text_files(english_path, persian_path):
    try:
        # Load text files into DataFrame
        with open(english_path, 'r', encoding='utf-8') as en_file:
            english_lines = en_file.readlines()
        with open(persian_path, 'r', encoding='utf-8') as fa_file:
            persian_lines = fa_file.readlines()

        # Combine into a DataFrame
        data = {'English': english_lines, 'Persian': persian_lines}
        df = pd.DataFrame(data)
        print(df)

        return df
    except Exception as e:
        print(f"Error loading text files: {e}")
        return None

# Function to delete records containing content within brackets in a specific column
def delete_records_with_brackets(df, column_name):
    try:
        # Compile regex pattern to detect content within brackets
        pattern = re.compile(r'\[.*?\]')  # Use raw string to avoid escape issues

        # Filter out rows where the column contains the unwanted patterns
        cleaned_df = df[~df[column_name].str.contains(pattern, na=False)].copy()

        return cleaned_df
    except re.error as e:
        # Print regex error and return the original DataFrame if an error occurs
        print(f"Regex error: {e}")
        return df

# Function to process a single file
def process_text_data(df):
    persian_processor = PersianTextPreprocessor()
    english_processor = EnglishTextPreprocessor()

    # try:
    # Process columns
    df['Cleaned_English'] = english_processor.process_column(df['English'])
    df['Cleaned_Persian'] = persian_processor.process_column(df['Persian'])

    # Remove records with brackets and other undesired content
    df = delete_records_with_brackets(df, 'Cleaned_English')
    df = delete_records_with_brackets(df, 'Cleaned_Persian')

    # Drop rows with empty or blank values
    df = df.dropna(how='any', ignore_index=True)
    df = df[~df.apply(lambda x: x.str.strip().eq('').any(), axis=1)]

    # Ensure rows where cleaned columns differ
    df_filtered = df[df['Cleaned_English'] != df['Cleaned_Persian']]

    # Finalize columns for saving
    df_final = df_filtered[['Cleaned_English', 'Cleaned_Persian']]
    df_final.columns = ['English', 'Persian']
    return df_final
    # except Exception as e:
    #     print(f"Error processing text data: {e}")
    #     return None


def save_cleaned_data(df, save_path):
    try:
        df.to_csv(save_path, index=False, encoding='utf-8')
        print(f"Cleaned data saved to {save_path}")
    except Exception as e:
        print(f"Error saving data: {e}")


def main():
    # Load the text data
    df = load_text_files(english_file_path, persian_file_path)
    if df is None:
        print("Failed to load files. Exiting.")
        return

    # Process the data
    cleaned_df = process_text_data(df)
    if cleaned_df is None:
        print("Data processing failed. Exiting.")
        return

    # Save the cleaned data
    cleaned_file_path = os.path.join(output_directory, "cleaned_data.csv")
    save_cleaned_data(cleaned_df, cleaned_file_path)


if __name__ == "__main__":
    main()
