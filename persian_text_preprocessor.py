import pandas as pd
import emoji
import unicodedata
import re
import jdatetime
from parsivar import Normalizer, Tokenizer, FindStems
from Dictionaries_Fa import (
    arabic_dict,
    num_dict,
    sign_dict_fa_phase_one,
    sign_dict_fa_phase_two,
    special_char_dict,
    month_dict
)


class ConvertPersianDate:
    def convert_persian_to_standard_digits(self, text):
        persian_to_standard = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
        return text.translate(persian_to_standard)

    def handle_persian_dates(self, text, convert_to_standard=False):
        text = self.convert_persian_to_standard_digits(text)

        def convert_date(match):
            if not convert_to_standard:
                return ""
            persian_date = match.group(0)
            try:
                persian_date_obj = jdatetime.datetime.strptime(persian_date, '%Y/%m/%d')
                gregorian_date_obj = persian_date_obj.togregorian()
                return gregorian_date_obj.strftime('%Y-%m-%d')
            except ValueError:
                return ""

        pattern = r'\d{4}/\d{2}/\d{2}'
        text = re.sub(pattern, convert_date, text)
        return text


class PersianTextPreprocessor:
    def __init__(self, stopword_file=None, task="default"):

        self.arabic_dict = arabic_dict
        self.num_dict = num_dict
        self.sign_dict_fa_phase_one = sign_dict_fa_phase_one
        self.sign_dict_fa_phase_two = sign_dict_fa_phase_two
        self.special_char_dict = special_char_dict
        self.month_dict = month_dict
        self.date_converter = ConvertPersianDate
        self.normalizer = Normalizer(statistical_space_correction=True)
        self.tokenizer = Tokenizer()
        self.stemmer = FindStems()
        self.stopwords = set()
        if stopword_file:
            with open(stopword_file, "r", encoding="utf-8") as file:
                self.stopwords = set(file.read().splitlines())

        self.task_config = {
            "default": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": "remove",
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "apply_dictionary_replacements_signs": True,
                "remove_english_words": True,
                "handle_persian_punctuation": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": True,
                "convert_numbers_to_words": True,
                "check_spell": True,
                "normalize_text": True,
                "remove_stopwords": True,
                "apply_stemming": False,
                # "apply_lemmatization": True,
                "remove_half_space": True,
                "clean_extra_spaces": True,
            },
            "translation": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": False,
                "handle_emojis": None,
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "apply_dictionary_replacements_signs": False,
                "remove_english_words": False,
                "handle_persian_punctuation": False,
                "separate_cases": False,
                "clean_punctuation": True,
                "remove_numbers_only": False,
                "convert_numbers_to_words": False,
                "check_spell": True,
                "normalize_text": False,
                "remove_stopwords": False,
                "apply_stemming": False,
                # "apply_lemmatization": False,
                "remove_half_space": True,
                "clean_extra_spaces": True,
            },
            "sentiment": {
                "lowercase": True,
                "normalize_unicode": False,
                "remove_accents": True,
                "handle_emojis": "sentiment",
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "apply_dictionary_replacements_signs": True,
                "remove_english_words": False,
                "handle_persian_punctuation": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": True,
                "convert_numbers_to_words": False,
                "check_spell": True,
                "normalize_text": True,
                "remove_stopwords": True,
                "apply_stemming": False,
                # "apply_lemmatization": True,
                "remove_half_space": True,
                "clean_extra_spaces": True,
            },
            "ner": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": 'replace',
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "apply_dictionary_replacements_signs": True,
                "remove_english_words": False,
                "handle_persian_punctuation": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": False,
                "convert_numbers_to_words": False,
                "check_spell": True,
                "normalize_text": True,
                "remove_stopwords": False,
                "apply_stemming": False,
                # "apply_lemmatization": False,
                "remove_half_space": True,
                "clean_extra_spaces": True,
            },
            "topic_modeling": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": 'remove',
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "apply_dictionary_replacements_signs": True,
                "remove_english_words": True,
                "handle_persian_punctuation": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": True,
                "convert_numbers_to_words": False,
                "normalize_text": True,
                "remove_stopwords": True,
                "check_spell": True,
                "apply_stemming": True,
                # "apply_lemmatization": True,
                "remove_half_space": True,
                "clean_extra_spaces": True,
            },
            "spam_detection": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "remove_url_html": True,
                "remove_elements": True,
                "handle_emojis": 'remove',
                "apply_dictionary_replacements": True,
                "apply_dictionary_replacements_signs": True,
                "remove_english_words": True,
                "handle_persian_punctuation": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": False,
                "convert_numbers_to_words": False,
                "normalize_text": True,
                "check_spell": True,
                "remove_stopwords": True,
                "apply_stemming": False,
                # "apply_lemmatization": True,
                "remove_half_space": True,
                "clean_extra_spaces": True,
            },
            "summarization": {
                "lowercase": True,
                "normalize_unicode": True,
                "remove_accents": True,
                "handle_emojis": 'remove',
                "remove_url_html": True,
                "remove_elements": True,
                "apply_dictionary_replacements": True,
                "apply_dictionary_replacements_signs": False,
                "remove_english_words": True,
                "handle_persian_punctuation": True,
                "separate_cases": True,
                "clean_punctuation": True,
                "remove_numbers_only": False,
                "convert_numbers_to_words": False,
                "check_spell": True,
                "normalize_text": True,
                "remove_stopwords": False,
                "apply_stemming": False,
                # "apply_lemmatization": True,
                "remove_half_space": True,
                "clean_extra_spaces": True,
            },
        }

        self.current_task_config = self.task_config.get(task, self.task_config["default"])

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

    def normalize_unicode(self, text):
        return unicodedata.normalize("NFKC", text) if isinstance(text, str) else text

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
        text = re.sub(r'%[a-zA-Z]+', '', text) # Remove time-related patterns like %i:%m %p, %a, %b
        text = re.sub(r'&[a-z]+;', '', text) # Remove HTML or encoded characters
        text = re.sub(r'\s+', ' ', text).strip() # Normalize spaces
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

    def pre_process_alphabet_numbers(self, text):
        text = text.lower()
        dictionaries = [
            self.sign_dict_fa_phase_one,
            self.arabic_dict,
            self.num_dict,
            self.special_char_dict,
        ]
        for dictionary in dictionaries:
            for key, value in dictionary.items():
                text = re.sub(re.escape(key), value, text)

        signs_and_symbols = r'[،؛؟٪…»«ـ!@#$%^&*()_+=\[\]{}|\\:;"\'<>,./؟]'
        text = re.sub(f'({signs_and_symbols})', r'\1 ', text) # Add space after each matched sign or symbol

        return text

    def clean_extra_spaces(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def pre_process_signs(self, text):
        text = text.lower()
        dictionaries = [
            self.sign_dict_fa_phase_two,
        ]
        for dictionary in dictionaries:
            for key, value in dictionary.items():
                text = re.sub(re.escape(key), value, text)
        return text

    def remove_half_space(self, text):
        pattern = r'(\u200C)(ای|دان|ها|می|تر|ترین)'
        text = re.sub(pattern, r' \2', text)
        text = re.sub(r'\s+', ' ', text).strip()
        text = text.replace('\u200C', '')
        return text

    def remove_numbers_only_cells(self, text):
        stripped_text = re.sub(r'[\s,]+', '', text)
        if stripped_text.isdigit():
            return ''
        return text

    def handle_emojis(self, text, strategy):
        if not isinstance(text, str):
            return text

        def remove_emojis(text):
            return ''.join(char for char in text if char not in emoji.EMOJI_DATA)

        def replace_emojis(text):
            return ''.join(char if char not in emoji.EMOJI_DATA else "[EMOJI]" for char in text)

        def sentiment_emojis(text):
            return ''.join(char if char not in emoji.EMOJI_DATA else " positive " for char in text)

        emoji_strategies = {
            "remove": remove_emojis,
            "replace": replace_emojis,
            "sentiment": sentiment_emojis,
        }
        result = emoji_strategies.get(strategy, lambda x: x)(text)
        return result

    def process_text(self, column):

        if isinstance(column, list):
            column = pd.Series(column)

        config = self.current_task_config
        # print("Config:", self.current_task_config)

        column = column.apply(self.remove_cyrillic)

        if config["lowercase"]:
            column = column.apply(self.to_lower_case)

        if config["remove_url_html"]:
            column = column.apply(self.remove_url)
            column = column.apply(self.remove_encoded_email_strings)
            column = column.apply(self.remove_html_tags)
            column = column.apply(self.remove_emails)

        column = column.apply(lambda x: ConvertPersianDate().handle_persian_dates(x, convert_to_standard=True))

        if config["remove_elements"]:
            column = column.apply(self.remove_elements)
        if config["apply_dictionary_replacements"]:
            column = column.apply(self.pre_process_alphabet_numbers)
        if config["apply_dictionary_replacements_signs"]:
            column = column.apply(self.pre_process_signs)
        if config['remove_english_words']:
            column = column.apply(self.remove_english_words)
        if config['handle_persian_punctuation']:
            column = column.apply(self.handle_persian_punctuation)
        if config["separate_cases"]:
            column = column.apply(self.separate_cases)
        if config["clean_punctuation"]:
            column = column.apply(self.clean_farsi_text_punctuation)
        if config["remove_numbers_only"]:
            column = column.apply(self.remove_numbers_only_cells)

        handle_emojis_strategy = config.get("handle_emojis")
        if handle_emojis_strategy:
            column = column.apply(lambda x: self.handle_emojis(x, handle_emojis_strategy))

        if config["normalize_text"]:
            column = column.apply(self.pre_process_alphabet_numbers)
        if config['remove_half_space']:
            column = column.apply(self.remove_half_space)
        if config["remove_stopwords"]:
            column = column.apply(lambda x: ' '.join(self.remove_stopwords(self.tokenizer.tokenize_words(x))))
        # if config["apply_stemming"]:
        #     column = column.apply(
        #         lambda x: ' '.join(self.stemmer.convert_to_stem(token) for token in self.tokenizer.tokenize_words(x)))
        # if config["apply_lemmatization"]:
        #     column = column.apply(
        #         lambda x: ' '.join(self.stemmer.convert_to_stem(token) for token in self.tokenizer.tokenize_words(x)))
        if config["clean_extra_spaces"]:
            column = column.apply(self.clean_extra_spaces)

        return column
