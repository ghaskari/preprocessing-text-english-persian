import os
import pandas as pd
import re
import argparse
from persian_text_preprocessor import PersianTextPreprocessor
from english_text_preprocessor import EnglishTextPreprocessor

english_file_path = "DataSource/GNOME.en-fa.en"
persian_file_path = "DataSource/GNOME.en-fa.fa"
output_directory = "DataSource"

def load_text_files(english_path, persian_path, output_path):
    try:
        with open(english_path, 'r', encoding='utf-8') as en_file:
            english_lines = en_file.readlines()
        with open(persian_path, 'r', encoding='utf-8') as fa_file:
            persian_lines = fa_file.readlines()

        data = {'English': english_lines, 'Persian': persian_lines}
        df = pd.DataFrame(data)
        df.to_csv(f'{output_path}', index=False)
        return df
    except Exception as e:
        print(f"Error loading text files: {e}")
        return None

def remove_rows_with_only_signs(df, column_name):
    signs_and_symbols = r'^[^\w\u0600-\u06FF]+$'
    mask = df.applymap(lambda x: bool(re.match(signs_and_symbols, str(x))) if isinstance(x, str) else False)
    return df[~mask.any(axis=1)]

def delete_records_with_brackets(df, column_name):
    pattern = re.compile(r'\[.*?\]')
    return df[~df[column_name].str.contains(pattern, na=False)].copy()

def process_text_data(df, task):
    persian_processor = PersianTextPreprocessor(task=task)
    english_processor = EnglishTextPreprocessor(task=task)

    df['Cleaned_English'] = english_processor.process_column(df['English'])
    df['Cleaned_Persian'] = persian_processor.process_text(df['Persian'])

    df = delete_records_with_brackets(df, 'Cleaned_English')
    df = delete_records_with_brackets(df, 'Cleaned_Persian')
    df = df.dropna(how='any').reset_index(drop=True)
    df = df[~df.apply(lambda x: x.str.strip().eq('').any(), axis=1)]

    df_filtered = df[df['Cleaned_English'] != df['Cleaned_Persian']]
    df_filtered = remove_rows_with_only_signs(df_filtered, 'Cleaned_English')
    df_filtered = remove_rows_with_only_signs(df_filtered, 'Cleaned_Persian')

    df_final = df_filtered[['Cleaned_English', 'Cleaned_Persian']]
    df_final.columns = ['English', 'Persian']
    return df_final

def save_cleaned_data(df, save_path):
    try:
        df.to_csv(save_path, index=False, encoding='utf-8')
        print(f"Cleaned data saved to {save_path}")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    parser = argparse.ArgumentParser(description="Process translation tasks.")
    parser.add_argument("--task", type=str, required=True,
                        choices=["default", "translation", "sentiment", "ner", "topic_modeling", "spam_detection",
                                 "summarization"],
                        help="Task configuration to use for processing.")
    args = parser.parse_args()

    # df = load_text_files(english_file_path, persian_file_path)
    df = pd.read_csv('DataSource/main_file_gnome.csv')
    if df is None:
        print("Failed to load files. Exiting.")
        return

    print(df)

    cleaned_df = process_text_data(df, args.task)
    if cleaned_df is None:
        print("Data processing failed. Exiting.")
        return

    cleaned_file_path = os.path.join(output_directory, f"cleaned_data_{args.task}.csv")
    save_cleaned_data(cleaned_df, cleaned_file_path)

if __name__ == "__main__":
    main()
