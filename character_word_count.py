import os
import pandas as pd


class WordCharacterCount:
    def __init__(self, output_directory="FrequencyCount"):
        """
        Initialize the WordCharacterCount class with the output directory.
        """
        self.output_directory = output_directory
        # Ensure the output directory exists
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def save_data_to_file(self, df, filename, file_type="csv"):
        """
        Save a DataFrame to a file (CSV or Excel) in the specified output directory.
        """
        filepath = os.path.join(self.output_directory, f"{filename}.{file_type}")
        if file_type == "csv":
            df.to_csv(filepath, index=False, encoding="utf-8")
        elif file_type == "xlsx":
            df.to_excel(filepath, index=False, engine="openpyxl")
        else:
            raise ValueError("Unsupported file type. Use 'csv' or 'xlsx'.")
        print(f"Saved {file_type.upper()} file to {filepath}")

    def word_count(self, data, file_name="word_frequency"):
        """
        Generate a word frequency count from the input data.

        Args:
            data (list): List of text strings to analyze.
            file_name (str): Base name for the output file.

        Returns:
            pd.DataFrame: DataFrame containing word frequencies.
        """
        word_freq = {}
        for row in data:
            # Split the text into words
            words = row.split()
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1

        # Convert to a DataFrame and sort by frequency
        word_freq_df = pd.DataFrame(
            list(word_freq.items()), columns=["Word", "Frequency"]
        ).sort_values(by="Frequency", ascending=False).reset_index(drop=True)

        # Save results to CSV and Excel
        self.save_data_to_file(word_freq_df, f"{file_name}_WordsCount", file_type="csv")
        self.save_data_to_file(word_freq_df, f"{file_name}_WordsCount", file_type="xlsx")

        return word_freq_df

    def character_count(self, data, file_name="char_frequency"):
        """
        Generate a character frequency count from the input data.

        Args:
            data (list): List of text strings to analyze.
            file_name (str): Base name for the output file.

        Returns:
            pd.DataFrame: DataFrame containing character frequencies.
        """
        char_freq = {}
        for row in data:
            for char in row:
                char_freq[char] = char_freq.get(char, 0) + 1

        # Convert to a DataFrame and sort by frequency
        char_freq_df = pd.DataFrame(
            list(char_freq.items()), columns=["Character", "Frequency"]
        ).sort_values(by="Frequency", ascending=False).reset_index(drop=True)

        # Save results to CSV and Excel
        self.save_data_to_file(char_freq_df, f"{file_name}_CharactersCount", file_type="csv")
        self.save_data_to_file(char_freq_df, f"{file_name}_CharactersCount", file_type="xlsx")

        return char_freq_df
