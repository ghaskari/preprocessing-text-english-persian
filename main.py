import os
import pandas as pd
import re
import argparse
from persian_text_preprocessor import PersianTextPreprocessor
from english_text_preprocessor import EnglishTextPreprocessor

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


def process_text_data(df, task, column=None):
    """
    Process text data for a specific task.
    """
    if task == "translation":
        if not {'English', 'Persian'}.issubset(df.columns):
            raise ValueError("Translation task requires both 'English' and 'Persian' columns.")
        persian_processor = PersianTextPreprocessor(task=task)
        english_processor = EnglishTextPreprocessor(task=task)

        # Process English and Persian columns
        df['Cleaned_English'] = english_processor.process_column(df['English'])
        df['Cleaned_Persian'] = persian_processor.process_text(df['Persian'])

        # Remove unwanted rows
        df = remove_rows_with_only_numbers(df, 'Cleaned_English')
        df = remove_rows_with_only_numbers(df, 'Cleaned_Persian')
        df = delete_records_with_brackets(df, 'Cleaned_English')
        df = delete_records_with_brackets(df, 'Cleaned_Persian')
        df = remove_rows_with_only_signs(df, 'Cleaned_English')
        df = remove_rows_with_only_signs(df, 'Cleaned_Persian')
        df = df.drop_duplicates(subset=['Cleaned_English', 'Cleaned_Persian'])

        # Keep only cleaned columns
        df_final = df[['Cleaned_English', 'Cleaned_Persian']]
        df_final.columns = ['English', 'Persian']
        return df_final
    else:
        if column not in df.columns:
            raise ValueError(f"The specified column '{column}' is not in the dataset.")

        processor = PersianTextPreprocessor(task=task) if task in ['ner', 'sentiment'] else EnglishTextPreprocessor(
            task=task)
        df[f'Cleaned_{column}'] = processor.process_column(df[column])

        df = remove_rows_with_only_numbers(df, f'Cleaned_{column}')
        df = delete_records_with_brackets(df, f'Cleaned_{column}')
        df = remove_rows_with_only_signs(df, f'Cleaned_{column}')
        df = df.drop_duplicates(subset=[f'Cleaned_{column}'])

        df_final = df[[f'Cleaned_{column}']]
        df_final.columns = [column]
        return df_final


def save_cleaned_data(df, save_path):
    """
    Save the cleaned data to a specified file path. Creates the directory if it doesn't exist.
    """
    try:
        # Extract directory from save_path and create it if it doesn't exist
        output_dir = os.path.dirname(save_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the data in both Excel and CSV formats
        df.to_excel(f'{save_path}.xlsx', index=False)
        df.to_csv(f'{save_path}.csv', index=False, encoding='utf-8')

        print(df)
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
    parser.add_argument("--column", type=str,
                        help="Column name to process (if task doesn't require both English and Persian).")
    parser.add_argument("--output", type=str, default=output_directory, help="Directory to save the cleaned data.")
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.input)
    except Exception as e:
        print(f"Error loading input file: {e}")
        return

    print("Loaded data:")
    print(df)

    try:
        cleaned_df = process_text_data(df, args.task, column=args.column)
        cleaned_file_path = os.path.join(args.output, f"cleaned_data_{args.task}")
        save_cleaned_data(cleaned_df, cleaned_file_path)
    except Exception as e:
        print(f"Error during processing: {e}")


if __name__ == "__main__":
    main()
