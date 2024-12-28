import re
import emoji
from datetime import datetime
from parsivar import Normalizer, Tokenizer, FindStems
from Dictionaries_Fa import (
    arabic_dict,
    num_dict,
    sign_dict_fa,
    english_dict,
    special_char_dict,
    month_dict
)


class convert_persian_date:
    def convert_persian_to_standard_digits(self, text):

        persian_to_standard = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
        return text.translate(persian_to_standard)

    def handle_persian_dates(self, text, convert_to_standard=False):

        text = self.convert_persian_to_standard_digits(text)

        def convert_date(match):
            if not convert_to_standard:
                return ''
            persian_date = match.group(0)
            try:
                # Convert Persian date string to Gregorian format
                date_obj = datetime.strptime(persian_date, '%Y/%m/%d')
                return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                return ''

        pattern = r'\d{4}/\d{2}/\d{2}'
        text = re.sub(pattern, convert_date, text)
        return text


class PersianTextPreprocessor:
    def __init__(self, stopword_file=None, task="default"):

        self.arabic_dict = arabic_dict
        self.num_dict = num_dict
        self.sign_dict_fa = sign_dict_fa
        self.english_dict = english_dict
        self.special_char_dict = special_char_dict
        self.month_dict = month_dict
        self.normalizer = Normalizer(statistical_space_correction=True)
        self.tokenizer = Tokenizer()
        self.stemmer = FindStems()
        self.stopwords = set()
        if stopword_file:
            with open(stopword_file, "r", encoding="utf-8") as file:
                self.stopwords = set(file.read().splitlines())


        # Task-specific configurations
        self.task_config = {
            "default": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": "replace",
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
                "handle_emojis": "sentiment",
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


    def spell_check(self, text):

        return self.normalizer.normalize(text)

    def remove_stopwords(self, tokens):

        return [token for token in tokens if token not in self.stopwords]

    def to_lower_case(self, text):
        text = text.lower()

        return text

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

    def remove_url(self, text):
        text = re.sub(r'http[s]?://\S+', '', text)  # Remove URLs starting with http or https
        text = re.sub(r'www\.\S+', '', text)  # Remove URLs starting with www
        text = re.sub(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s]*)?\b', '',
                      text)  # Remove URLs without protocol (e.g., example.com)
        return text

    def remove_html_tags(self, text):
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'<.*?>+', '', text)

        return text

    def remove_encoded_email_strings(self, text):
        text = re.sub(r'[^\x00-\x7F]+<[\w\.\-]+@[\w\.\-]+\.[a-zA-Z]{2,}>', '', text)
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)

        return text

    def remove_emails(self, text):
        text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '', text)
        text = re.sub(r'[^\x00-\x7F]+<[\w\.\-]+@[\w\.\-]+\.[a-zA-Z]{2,}>', '', text)
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)

        return text

    def remove_elements(self, text):

        if isinstance(text, float):
            return ''

        text = re.sub(r'@\w+', '', text)  # Remove mentions
        text = re.sub(r'#\w+', '', text)  # Remove hashtags
        text = re.sub(r'@(\w+\.)*\w+', '', text)  # Remove mentions followed by a dot
        text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
        text = re.sub(r'\b\d{1,3}(?:\.\d{1,3}){3}\b(?:\:\d+)?', '', text)  # Handle IP addresses with optional port numbers
        text = text.replace('\n', ' ')  # Replace newline characters with a space
        text = text.lower()  # Convert all text to lowercase

        return text

    def handle_persian_punctuation(self, text):

        text = re.sub(r'\s+', ' ', text)

        text = text.strip()

        return text

    def clean_farsi_text_punctuation(self, text):

        text = re.sub(r'\s+', ' ', text) # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        text = re.sub(r'\.(?=\S)', '. ', text)  # Ensure space after a period
        text = re.sub(r'\b\d{1,2} [A-Za-z]+ \d{4}\b', '', text)  # Remove dates (e.g., "1 July 1818")
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text).strip()  # Final cleanup of extra spaces

        return text

    def remove_english_words(self, persian_text):
        pattern = r'[a-zA-Z]'

        cleaned_text = re.sub(pattern, '', persian_text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

        return cleaned_text

    def remove_cyrillic(self, text):
        cyrillic_pattern = r'[\u0400-\u04FF\u0500-\u052F\u2DE0-\u2DFF\uA640-\uA69F]+'
        cleaned_text = re.sub(cyrillic_pattern, '', text)
        return cleaned_text

    def pre_process(self, text):
        text = text.lower()
        dictionaries = [
            self.sign_dict_fa,
            self.arabic_dict,
            self.num_dict,
            self.english_dict,
            self.special_char_dict,
        ]
        for dictionary in dictionaries:
            for key, value in dictionary.items():
                text = re.sub(re.escape(key), value, text)

        return text

    def remove_half_space(self, text):
        pattern = r'(\u200C)(ها|می|تر|ترین)'

        text = re.sub(pattern, r' \2', text)
        text = text.replace('\u200C', '')

        return text

    def remove_numbers_only_cells(self, text):
        stripped_text = re.sub(r'[\s,]+', '', text)

        if stripped_text.isdigit():
            return ''
        return text

    def remove_emoji(self, text):
        return ''.join(char for char in text if char not in emoji.EMOJI_DATA)

    def process_text(self, text):
        config = self.current_task_config

        if config["lowercase"]:
            text = self.to_lower_case(text)
        if config["remove_url_html"]:
            text = self.remove_url(text)
            text = self.remove_html_tags(text)
        if config["remove_elements"]:
            text = self.remove_elements(text)
        if config["apply_dictionary_replacements"]:
            text = self.pre_process(text)
        if config["separate_cases"]:
            text = self.separate_cases(text)
        if config["clean_punctuation"]:
            text = self.clean_farsi_text_punctuation(text)
        if config["remove_numbers_only"]:
            text = self.remove_numbers_only_cells(text)
        if config["normalize_text"]:
            text = self.spell_check(text)
        if config["remove_stopwords"]:
            tokens = self.tokenizer.tokenize_words(text)
            tokens = self.remove_stopwords(tokens)
            text = ' '.join(tokens)
        if config["apply_stemming"]:
            tokens = self.tokenizer.tokenize_words(text)
            text = ' '.join(self.stemmer.convert_to_stem(token) for token in tokens)
        if config["apply_lemmatization"]:
            tokens = self.tokenizer.tokenize_words(text)
            text = ' '.join(self.stemmer.convert_to_stem(token) for token in tokens)
        if config["clean_extra_spaces"]:
            text = re.sub(r'\s+', ' ', text).strip()

        if config["handle_emojis"] == "remove":
            text = self.remove_emoji(text)

        elif config["handle_emojis"] == "replace":
            text = ''.join(char if char not in emoji.EMOJI_DATA else "[EMOJI]" for char in text)
        elif config["handle_emojis"] == "sentiment":
            text = ''.join(char if char not in emoji.EMOJI_DATA else "positive" for char in text)

        return text

class ColumnProcessor:

    def __init__(self, text_preprocessor, date_converter):
        self.text_preprocessor = text_preprocessor
        self.date_converter = date_converter

    # def process_column(self, column):
    #     column = column.apply(self.text_preprocessor.to_lower_case)  # Convert to lowercase
    #     column = column.apply(self.text_preprocessor.remove_elements)  # Clean mentions, hashtags, etc.
    #     column = column.apply(self.text_preprocessor.remove_url)  # Remove URLs
    #     column = column.apply(self.text_preprocessor.remove_encoded_email_strings)  # Remove encoded emails
    #     column = column.apply(self.text_preprocessor.remove_html_tags)  # Remove HTML tags
    #     column = column.apply(self.text_preprocessor.remove_emails)  # Remove standard emails
    #     column = column.apply(self.text_preprocessor.remove_emails) # Remove emoji
    #     column = column.apply(self.text_preprocessor.pre_process)  # Apply dictionary-based corrections
    #     column = column.apply(self.text_preprocessor.separate_cases)  # Handle mixed-case/letter-number joins
    #     column = column.apply(self.text_preprocessor.remove_english_words)  # Remove English words
    #     column = column.apply(self.text_preprocessor.handle_persian_punctuation)  # Fix punctuation spacing
    #     column = column.apply(self.text_preprocessor.clean_farsi_text_punctuation)  # Clean text punctuation
    #     column = column.apply(self.text_preprocessor.remove_cyrillic)  # Remove Cyrillic characters
    #     column = column.apply(self.text_preprocessor.remove_numbers_only_cells)  # Remove numeric-only cells
    #     column = column.apply(self.text_preprocessor.remove_half_space)  # Handle Persian half-spaces
    #     column = column.apply(self.text_preprocessor.spell_check)  # Spell-check and normalize with Parsivar
    #     column = column.apply(self.date_converter.convert_persian_to_standard_digits)
    #     column = column.apply(lambda text: ' '.join(
    #         self.text_preprocessor.stemmer.convert_to_stem(token)
    #         for token in self.text_preprocessor.remove_stopwords(
    #             self.text_preprocessor.tokenizer.tokenize_words(text)
    #         )
    #     ))
    #     return column

    def process_column(self, column):
        return column.apply(self.text_preprocessor.process_text)
