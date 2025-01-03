import os
import pandas as pd
import re
import argparse
from persian_text_preprocessor import PersianTextPreprocessor
from english_text_preprocessor import EnglishTextPreprocessor

# Output directory for cleaned data
output_directory = "DataSource"


def remove_rows_with_only_signs(df, column_name):
    """
    Remove rows where the specified column contains only signs or symbols.
    """
    signs_and_symbols = r'^[^\w\u0600-\u06FF]+$'
    mask = df[column_name].apply(lambda x: bool(re.match(signs_and_symbols, str(x))) if isinstance(x, str) else False)

    return df[~mask]


def remove_rows_with_only_numbers(df, column_name):
    """
    Remove rows where the specified column contains only numbers.
    """
    numbers_pattern = r'^\d+$'  # Matches cells that contain only digits
    mask = df[column_name].apply(lambda x: bool(re.match(numbers_pattern, str(x))) if isinstance(x, str) else False)

    return df[~mask]


def delete_records_with_brackets(df, column_name):
    """
    Remove rows where the specified column contains text within brackets.
    """
    pattern = re.compile(r'\[.*?\]')
    return df[~df[column_name].str.contains(pattern, na=False)]


def process_text_data(df, task):
    """
    Process text data for a specific task.
    """
    persian_processor = PersianTextPreprocessor(task=task)
    english_processor = EnglishTextPreprocessor(task=task)

    # Process English and Persian columns
    df['Cleaned_English'] = english_processor.process_column(df['English'])
    df['Cleaned_Persian'] = persian_processor.process_text(df['Persian'])

    # Remove rows with only numbers
    df = remove_rows_with_only_numbers(df, 'Cleaned_English')
    df = remove_rows_with_only_numbers(df, 'Cleaned_Persian')

    # Remove rows with text in brackets
    df = delete_records_with_brackets(df, 'Cleaned_English')
    df = delete_records_with_brackets(df, 'Cleaned_Persian')

    # Drop rows with NA values and empty strings
    df = df.dropna(how='any').reset_index(drop=True)
    df = df[~df.apply(lambda x: x.str.strip().eq('').any(), axis=1)]

    # Remove rows with only signs or symbols
    df = remove_rows_with_only_signs(df, 'Cleaned_English')
    df = remove_rows_with_only_signs(df, 'Cleaned_Persian')
    df = df.drop_duplicates(subset=['Cleaned_English', 'Cleaned_Persian'])

    # Keep only cleaned columns
    df_final = df[['Cleaned_English', 'Cleaned_Persian']]
    df_final.columns = ['English', 'Persian']
    return df_final


def save_cleaned_data(df, save_path):
    """
    Save the cleaned data to a specified file path.
    """
    try:
        df.to_csv(save_path, index=False, encoding='utf-8')
        print(f"Cleaned data saved to {save_path}")
    except Exception as e:
        print(f"Error saving data: {e}")


def main():
    """
    Main function to process data based on a specific task.
    """
    parser = argparse.ArgumentParser(description="Process translation tasks.")
    parser.add_argument("--task", type=str, required=True,
                        choices=["default", "translation", "sentiment", "ner", "topic_modeling", "spam_detection",
                                 "summarization"],
                        help="Task configuration to use for processing.")
    parser.add_argument("--input", type=str, required=True, help="Path to the input CSV file.")
    parser.add_argument("--output", type=str, default=output_directory, help="Directory to save the cleaned data.")
    args = parser.parse_args()

    # Load the input CSV file
    try:
        df = pd.read_csv(args.input)
    except Exception as e:
        print(f"Error loading input file: {e}")
        return

    print("Loaded data:")
    print(df)

    # Process the text data for the specified task
    cleaned_df = process_text_data(df, args.task)
    if cleaned_df is None:
        print("Data processing failed. Exiting.")
        return

    # Save the cleaned data
    cleaned_file_path = os.path.join(args.output, f"cleaned_data_{args.task}.csv")
    save_cleaned_data(cleaned_df, cleaned_file_path)


if __name__ == "__main__":
    main()
