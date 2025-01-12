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
                "apply_normalization": False,
                "clean_punctuation": True,
                "remove_stopwords": True,
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
                "apply_dictionary_replacements": True,
                "apply_normalization": False,
                "clean_punctuation": False,
                "remove_stopwords": False,
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
                "apply_normalization": True,
                "clean_punctuation": True,
                "remove_stopwords": True,
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
                "apply_normalization": True,
                "clean_punctuation": True,
                "remove_stopwords": False,
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
                "apply_normalization": True,
                "clean_punctuation": True,
                "remove_stopwords": True,
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
                "apply_normalization": True,
                "clean_punctuation": True,
                "remove_stopwords": True,
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
                "apply_normalization": True,
                "clean_punctuation": True,
                "remove_stopwords": False,
                "apply_lemmatization": True,
                "clean_extra_spaces": True,
            },
        }
        self.current_task_config = self.task_config.get(task, self.task_config["default"])

    def to_lower_case(self, text):
        return text.lower() if isinstance(text, str) else text

    def clean_text_percent_elements(self, text):
        text = re.sub(r'%[a-zA-Z]+', '', text) # Remove time-related patterns like %i:%m %p, %a, %b
        text = re.sub(r'&[a-z]+;', '', text) # Remove HTML or encoded characters
        text = re.sub(r'\s+', ' ', text).strip() # Normalize spaces

       # text = re.sub(r'[^\w\s\u0600-\u06FF]', '', text)  # Keeps Persian and English characters only

        return text

    def normalize_unicode(self, text):
        return unicodedata.normalize("NFKC", text) if isinstance(text, str) else text

    def remove_accents(self, text):
        return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))

    def correct_spelling(self, text):
        corrected_text = []
        misspelled_words = self.spellchecker.unknown(text.split())
        for word in text.split():
            corrected_text.append(self.spellchecker.correction(word) if word in misspelled_words else word)
        return " ".join(corrected_text)

    def handle_emojis(self, text, strategy="remove"):
        if strategy == "remove":
            return emoji.replace_emoji(text, "")
        elif strategy == "replace":
            return emoji.demojize(text)
        elif strategy == "sentiment":
            emoji_sentiment_map = {
                "😊": "positive",
                "😢": "negative",
                "😂": "positive",
                "😐": "neutral",
            }
            for emoji_char, sentiment in emoji_sentiment_map.items():
                text = text.replace(emoji_char, sentiment)
            return text
        else:
            return text

    def remove_url_and_html(self, text):
        text = re.sub(r"http[s]?://\S+", "", text)  # Remove URLs
        text = re.sub(r"<.*?>", "", text)  # Remove HTML tags
        return self.clean_extra_spaces(text)

    def remove_elements(self, text):
        text = re.sub(r"@\w+", "", text)  # Remove mentions
        text = re.sub(r"#\w+", "", text)  # Remove hashtags
        return self.clean_extra_spaces(text)

    def clean_punctuation(self, text):
        return re.sub(r"[^\w\s]", "", text)

    def clean_extra_spaces(self, text):
        text = text.replace('\n', ' \n ')
        # text = text.replace('\n', ' ')
        text =  re.sub(r'\s+', ' ', text).strip()
        return text

    def apply_dictionaries(self, text, dictionaries):
        for dictionary in dictionaries:
            for key, value in dictionary.items():
                text = text.replace(key, value)

        # text = re.sub(r'([^\w\s])', r'\1 ', text)  # Add a space after every character
        return text

    def remove_stopwords(self, tokens):
        tokens = [re.sub(r"[^\w\s]", "", word) for word in tokens]  # Clean punctuation
        return [word for word in tokens if word.lower() not in self.stopwords]

    def apply_lemmatization(self, tokens):
        doc = self.nlp(" ".join(tokens))
        return [token.lemma_ for token in doc]

    def process_column(self, column):
        config = self.current_task_config

        if config["lowercase"]:
            column = column.apply(self.to_lower_case)

        if config["remove_url_html"]:
            column = column.apply(self.remove_url_and_html)

        if config["remove_elements"]:
            column = column.apply(self.remove_elements)

        if config["apply_dictionary_replacements"]:
            dictionaries = [
                    self.contractions_dict,
                    self.english_dict,
                    # self.sign_dict_en,
                    self.special_char_dict
            ]
            column = column.apply(lambda x: self.apply_dictionaries(x, dictionaries))

        if config["clean_punctuation"]:
            column = column.apply(self.clean_punctuation)

        if config["normalize_unicode"]:
            column = column.apply(self.normalize_unicode)

        if config["remove_accents"]:
            column = column.apply(self.remove_accents)

        if config["handle_emojis"]:
            column = column.apply(lambda x: self.handle_emojis(x, strategy=config["handle_emojis"]))

        if config["correct_spelling"]:
            column = column.apply(self.correct_spelling)

        if config["apply_normalization"]:
            column = column.apply(self.normalize_unicode)

        if config["remove_stopwords"]:
            column = column.apply(lambda x: " ".join(self.remove_stopwords(x.split())))

        if config["apply_lemmatization"]:
            column = column.apply(lambda x: " ".join(self.apply_lemmatization(x.split())))

        if config["clean_extra_spaces"]:
            column = column.apply(self.clean_extra_spaces)

        return column
