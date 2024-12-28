import re
from num2words import num2words
from spellchecker import SpellChecker
import unicodedata
import emoji
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from Dictionaries_En import (english_dict,
                             contractions_dict,
                             sign_dict_en,
                             special_char_dict,
                             month_dict)


class EnglishTextPreprocessor:
    def __init__(self, task="default"):
        self.stopwords = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.spellchecker = SpellChecker()
        self.english_dict = english_dict
        self.contractions_dict = contractions_dict
        self.sign_dict_en = sign_dict_en
        self.special_char_dict = special_char_dict
        self.month_dict = month_dict

        # Define task-specific configurations
        self.task_config = {
            "default": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": "replace",  # Options: "remove", "replace", "sentiment", None
                "correct_spelling": True,
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": True,
                "convert_numbers_to_words": True,
                "normalize_text": True,
                "remove_stopwords": True,
                "apply_stemming": False,
                "apply_lemmatization": True,
                "clean_extra_spaces": True,
            },
            "translation": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": False,
                "handle_emojis": None,
                "correct_spelling": False,
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": False,
                "separate_cases": False,
                "clean_punctuation": True,
                "remove_numbers_only": False,
                "convert_numbers_to_words": False,
                "normalize_text": False,
                "remove_stopwords": False,
                "apply_stemming": False,
                "apply_lemmatization": False,
                "clean_extra_spaces": True,
            },
            "sentiment": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": "sentiment",  # Convert emojis to sentiment words
                "correct_spelling": True,
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": True,
                "convert_numbers_to_words": False,
                "normalize_text": True,
                "remove_stopwords": True,
                "apply_stemming": False,
                "apply_lemmatization": True,
                "clean_extra_spaces": True,
            },
            "ner": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": None,
                "correct_spelling": False,
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": False,
                "convert_numbers_to_words": False,
                "normalize_text": True,
                "remove_stopwords": False,
                "apply_stemming": False,
                "apply_lemmatization": False,
                "clean_extra_spaces": True,
            },
            "topic_modeling": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": None,
                "correct_spelling": False,
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": True,
                "convert_numbers_to_words": False,
                "normalize_text": True,
                "remove_stopwords": True,
                "apply_stemming": True,
                "apply_lemmatization": True,
                "clean_extra_spaces": True,
            },
            "spam_detection": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": None,
                "correct_spelling": True,
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": False,
                "convert_numbers_to_words": False,
                "normalize_text": True,
                "remove_stopwords": True,
                "apply_stemming": False,
                "apply_lemmatization": True,
                "clean_extra_spaces": True,
            },
            "summarization": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": None,
                "correct_spelling": False,
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": False,
                "convert_numbers_to_words": False,
                "normalize_text": True,
                "remove_stopwords": False,
                "apply_stemming": False,
                "apply_lemmatization": True,
                "clean_extra_spaces": True,
            },
        }

        self.current_task_config = self.task_config.get(task, self.task_config["default"])

    def to_lower_case(self, text):
        return text.lower()  # Convert text to lowercase

    def normalize_unicode(self, text):
        return unicodedata.normalize('NFKC', text)

    def remove_accents(self, text):
        return ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))

    def correct_spelling(self, text):
        spell = SpellChecker()

        corrected_text = []
        misspelled_words = spell.unknown(text.split())
        for word in text.split():
            if word in misspelled_words:
                corrected_text.append(spell.correction(word))
            else:
                corrected_text.append(word)
        return " ".join(corrected_text)

    def remove_emojis(self, text):
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # Emoticons
            u"\U0001F300-\U0001F5FF"  # Symbols & Pictographs
            u"\U0001F680-\U0001F6FF"  # Transport & Map Symbols
            u"\U0001F1E0-\U0001F1FF"  # Flags
            u"\U00002700-\U000027BF"  # Dingbats
            u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
            u"\U00002600-\U000026FF"  # Miscellaneous Symbols
            u"\U00002B50-\U00002B55"  # Additional symbols
            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    def replace_emojis_with_text(self, text):
        return emoji.demojize(text)  # Replaces emojis with their textual description

    def map_emojis_to_sentiment(self, text):
        emoji_sentiment_map = {
            "😊": "positive",
            "😢": "negative",
            "😂": "positive",
            "😐": "neutral",
        }
        for emoji_char, sentiment in emoji_sentiment_map.items():
            text = text.replace(emoji_char, sentiment)
        return text

    def handle_emojis(self, text, strategy="remove"):
        if strategy == "remove":
            return self.remove_emojis(text)
        elif strategy == "replace":
            return self.replace_emojis_with_text(text)
        elif strategy == "sentiment":
            return self.map_emojis_to_sentiment(text)
        else:
            return text

    def remove_url_and_html(self, text):
        text = re.sub(r'http[s]?://\S+', '', text)  # Remove URLs
        text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)  # Remove URLs with newlines
        text = re.sub(r'www\.\S+', '', text)  # Remove URLs starting with www
        text = re.sub(r'<.*?>+', '', text)  # Remove HTML tags

        # Remove IP addresses (e.g., 192.168.0.1)
        text = re.sub(r'\b\d{1,3}(?:\.\d{1,3}){3}\b(?:\:\d+)?', '', text)  # Handle IP addresses

        # Remove email addresses
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)  # Remove email addresses

        return text

    def remove_elements(self, text):
        if isinstance(text, float):
            return ''

        text = re.sub(r'@\w+', '', text)  # Remove mentions
        text = re.sub(r'#\w+', '', text)  # Remove hashtags
        text = text.replace('\n', ' ')  # Replace newline characters with a space
        text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
        return text

    def remove_punc(self, text):
        return re.sub(r"[^\w\s]", "", text)  # Remove punctuation

    def separate_cases(self, text):
        if len(text) <= 1:
            return ' '
        new_text = ""
        last_char_all_num = text[0].isalnum()

        for char in text:
            if char.isalnum() != last_char_all_num and char.isalnum():
                new_text += " " + char
            else:
                new_text += char
            last_char_all_num = char.isalnum()
        return new_text

    def clean_english_text_punctuation(self, text):
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        text = re.sub(r'\s([?.!,":;](?:\s|$))', r'\1', text)  # Remove spaces before punctuation
        text = re.sub(r'\.(?=\S)', '. ', text)  # Ensure space after a period
        text = re.sub(r'\b\d{1,2} [A-Za-z]+ \d{4}\b', '', text)  # Remove dates (e.g., "1 July 1818")
        text = re.sub(r'\s*,\s*', ', ', text)  # Clean up commas
        text = re.sub(r'\s*\.\s*', '. ', text)  # Clean up periods
        text = re.sub(r'\s*\-\s*', '-', text)  # Clean up hyphens
        text = re.sub(r'\s+', ' ', text).strip()  # Final cleanup of extra spaces
        return text

    def replace_months(self, text):
        if not isinstance(text, str):
            return ''
        for short, full in self.month_dict.items():
            text = re.sub(rf'\b{short}\b', full, text)
        return text

    def apply_dictionary_replacements(self, text):
        dictionaries_eng = [
            self.contractions_dict,
            self.english_dict,
            self.sign_dict_en,
            self.special_char_dict
        ]
        for dictionary in dictionaries_eng:
            for key, value in dictionary.items():
                text = re.sub(re.escape(key), value, text)
        return text

    def remove_numbers_only_cells(self, text):
        stripped_text = re.sub(r'[\s,]+', '', text)
        if stripped_text.isdigit():
            return ''
        return text

    def convert_numbers_to_words_en(self, text):
        return re.sub(r'\d+', lambda x: num2words(int(x.group()), lang='en'), text)

    def normalize_text(self, text):
        tokens = word_tokenize(text)
        return tokens

    def remove_stopwords(self, tokens):
        return [word for word in tokens if word not in self.stopwords]

    def apply_stemming(self, tokens):
        return [self.stemmer.stem(word) for word in tokens]

    def apply_lemmatization(self, tokens):
        return [self.lemmatizer.lemmatize(word) for word in tokens]

    def clean_extra_spaces(self, text):
        return re.sub(r"\s+", ' ', text).strip()

    def process_column(self, column):
        config = self.current_task_config

        if config["lowercase"]:
            column = column.apply(self.to_lower_case)
        if config["normalize_unicode"]:
            column = column.apply(self.normalize_unicode)
        if config["remove_accents"]:
            column = column.apply(self.remove_accents)
        if config["handle_emojis"]:
            column = column.apply(lambda x: self.handle_emojis(x, strategy=config["handle_emojis"]))
        if config["correct_spelling"]:
            column = column.apply(self.correct_spelling)
        if config["remove_url_html"]:
            column = column.apply(self.remove_url_and_html)
        if config["remove_elements"]:
            column = column.apply(self.remove_elements)
        if config["apply_dictionary_replacements"]:
            column = column.apply(self.apply_dictionary_replacements)
        if config["separate_cases"]:
            column = column.apply(self.separate_cases)
        if config["clean_punctuation"]:
            column = column.apply(self.clean_english_text_punctuation)
        if config["remove_numbers_only"]:
            column = column.apply(self.remove_numbers_only_cells)
        if config["convert_numbers_to_words"]:
            column = column.apply(self.convert_numbers_to_words_en)
        if config["normalize_text"]:
            column = column.apply(self.normalize_text)
        if config["remove_stopwords"]:
            column = column.apply(self.remove_stopwords)
        if config["apply_stemming"]:
            column = column.apply(self.apply_stemming)
        if config["apply_lemmatization"]:
            column = column.apply(self.apply_lemmatization)
        column = column.apply(lambda x: ' '.join(x) if isinstance(x, list) else x)
        if config["clean_extra_spaces"]:
            column = column.apply(self.clean_extra_spaces)

        return column
