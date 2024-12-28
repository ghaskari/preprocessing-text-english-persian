import pandas as pd


class WordCharacterCount:
    def save_data_to_excel(self, df, filename):
        filename = f"FrequencyCount/{filename}.xlsx"
        df.to_excel(filename, index=False)

    def save_data_to_csv(self, df, filename):
        filename = f"FrequencyCount/{filename}.csv"
        df.to_csv(filename, index=False)

    def word_count(self, data, file_name=''):
        word_freq = {}
        for row in data:
        # split the text into words
            words = row.split(' ')
            # iterate over each word
            for word in words:
                # if the word is already in the dictionary, increase its count by 1
                if word in word_freq:
                    word_freq[word] += 1
            # if the word is not in the dictionary, add it and set its count to 1
                else:
                    word_freq[word] = 1

        # convert the dictionary into a dataframe and sort by the word frequency
        word_freq_df = pd.DataFrame(list(word_freq.items()), columns=['word', 'frequency']).sort_values('frequency', ascending=False).reset_index(drop=True)
        self.save_data_to_excel(word_freq_df, f'WordsCount_{file_name}')
        return word_freq_df

    def character_count(self, data, file_name):
        characters_freq = {}
        # iterate over each row in the data
        for row in data:
            # get the comment from the row
            comment = row
            # iterate over each character in the comment
            for character in comment:
                # if the character is already in the dictionary, increase its count by 1
                if character in characters_freq:
                    characters_freq[character] += 1
                # if the character is not in the dictionary, add it and set its count to 1
                else:
                    characters_freq[character] = 1

        # convert the dictionary into a dataframe and sort by the character frequency
        character_freq_df = pd.DataFrame(list(characters_freq.items()), columns=['Character', 'Frequency']).sort_values('Frequency', ascending=False).reset_index(drop=True)
        self.save_data_to_excel(character_freq_df, f'CharactersCount_{file_name}')

        return character_freq_df
