import re
import unicodedata
import emoji
from spellchecker import SpellChecker
import spacy

from Dictionaries_En import (
    english_dict,
    contractions_dict,
    sign_dict_en,
    special_char_dict,
    month_dict,
)

class EnglishTextPreprocessor:
    def __init__(self, task="default"):
        self.spellchecker = SpellChecker()
        self.english_dict = english_dict
        self.contractions_dict = contractions_dict
        self.sign_dict_en = sign_dict_en
        self.special_char_dict = special_char_dict
        self.month_dict = month_dict

        self.nlp = spacy.load("en_core_web_sm")
        self.stopwords = self.nlp.Defaults.stop_words


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
        if isinstance(text, str):
            return text.lower()
        return text

    def clean_extra_spaces(self, text):
        return re.sub(r"\s+", ' ', text).strip()

    def normalize_unicode(self, text):
        if isinstance(text, str):
            return unicodedata.normalize("NFKC", text)
        return text

    def remove_accents(self, text):
        return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))

    def correct_spelling(self, text):
        corrected_text = []
        misspelled_words = self.spellchecker.unknown(text.split())
        for word in text.split():
            if word in misspelled_words:
                correction = self.spellchecker.correction(word)
                corrected_text.append(correction if correction else word)
            else:
                corrected_text.append(word)
        return " ".join(corrected_text)

    def remove_emojis(self, text):
        return emoji.replace_emoji(text, "")

    def replace_emojis_with_text(self, text):
        return emoji.demojize(text)

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

    def apply_dictionaries(self, text, dictionaries):
        for dictionary in dictionaries:
            for key, value in dictionary.items():
                text = text.replace(key, value)
        return text

    def debug_text_processing(self, text, dictionaries):

        for dictionary in dictionaries:
            for key, value in dictionary.items():
                if key in text:
                    print(f"Replacing '{key}' with '{value}' in text: {text}")
                    text = re.sub(rf'\b{re.escape(key)}\b', value, text)
        return text

    def remove_url_and_html(self, text):
        text = re.sub(r"http[s]?://\S+", "", text)  # Remove URLs
        text = re.sub(r"<.*?>", "", text)  # Remove HTML tags
        return text

    def remove_elements(self, text):
        text = re.sub(r"@\w+", "", text)  # Remove mentions
        text = re.sub(r"#\w+", "", text)  # Remove hashtags
        return text

    def clean_punctuation(self, text):
        return re.sub(r"[^\w\s]", "", text)

    def normalize_text(self, text):
        doc = self.nlp(text)
        return [token.text for token in doc]

    def remove_stopwords(self, tokens):
        return [word for word in tokens if word.lower() not in self.stopwords]

    def apply_lemmatization(self, tokens):
        doc = self.nlp(" ".join(tokens))
        return [token.lemma_ for token in doc]

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

        if config["clean_punctuation"]:
            column = column.apply(self.clean_punctuation)

        if config["apply_dictionary_replacements"]:
            dictionaries = [self.english_dict, self.contractions_dict, self.sign_dict_en, self.special_char_dict]
            column = column.apply(lambda x: self.apply_dictionaries(x, dictionaries))
        column = column.apply(self.normalize_text)

        if config["remove_stopwords"]:
            column = column.apply(self.remove_stopwords)

        if config["apply_lemmatization"]:
            column = column.apply(self.apply_lemmatization)
        column = column.apply(lambda x: ' '.join(x) if isinstance(x, list) else x)

        if config["clean_extra_spaces"]:
            column = column.apply(self.clean_extra_spaces)

        return column
