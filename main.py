import os
import pandas as pd
import re

from persian_text_preprocessor import PersianTextPreprocessor
from english_text_preprocessor import EnglishTextPreprocessor

english_file_path = "DataSource/GNOME.en-fa.en"
persian_file_path = "DataSource/GNOME.en-fa.fa"
output_directory = "DataSource"


def load_text_files(english_path, persian_path):
    try:
        with open(english_path, 'r', encoding='utf-8') as en_file:
            english_lines = en_file.readlines()
        with open(persian_path, 'r', encoding='utf-8') as fa_file:
            persian_lines = fa_file.readlines()

        data = {'English': english_lines, 'Persian': persian_lines}
        df = pd.DataFrame(data)
        print(df)

        return df
    except Exception as e:
        print(f"Error loading text files: {e}")
        return None

def delete_records_with_brackets(df, column_name):
    try:
        pattern = re.compile(r'\[.*?\]')

        cleaned_df = df[~df[column_name].str.contains(pattern, na=False)].copy()

        return cleaned_df
    except re.error as e:
        print(f"Regex error: {e}")
        return df


def process_text_data(df):

    persian_processor = PersianTextPreprocessor(task='translation')
    english_processor = EnglishTextPreprocessor(task='translation')

    # try:
    df['Cleaned_English'] = english_processor.process_column(df['English'])
    df['Cleaned_Persian'] = persian_processor.process_text(df['Persian'])

    df = delete_records_with_brackets(df, 'Cleaned_English')
    df = delete_records_with_brackets(df, 'Cleaned_Persian')

    df = df.dropna(how='any', ignore_index=True)
    df = df[~df.apply(lambda x: x.str.strip().eq('').any(), axis=1)]

    df_filtered = df[df['Cleaned_English'] != df['Cleaned_Persian']]

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
    df = load_text_files(english_file_path, persian_file_path)
    if df is None:
        print("Failed to load files. Exiting.")
        return
    df = df.iloc[36870:,:]
    print(df)

    cleaned_df = process_text_data(df)
    if cleaned_df is None:
        print("Data processing failed. Exiting.") 
        return

    cleaned_file_path = os.path.join(output_directory, "cleaned_data.csv")
    save_cleaned_data(cleaned_df, cleaned_file_path)
    print(cleaned_df)


if __name__ == "__main__":
    main()
