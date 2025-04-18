import unittest
import pandas as pd
from english_text_preprocessor import EnglishTextPreprocessor
from persian_text_preprocessor import PersianTextPreprocessor, ConvertPersianDate


class TestPersianTextPreprocessor(unittest.TestCase):

    def setUp(self):
        self.preprocessor = PersianTextPreprocessor()
        self.date_converter = ConvertPersianDate()

    def test_remove_url(self):
        text = "Check this link: https://example.com and this www.test.com"
        expected = "Check this link:  and this "
        result = self.preprocessor.remove_url(text)
        self.assertEqual(result, expected)

    def test_remove_html_tags(self):
        text = "This is a <b>bold</b> statement."
        expected = "This is a bold statement."
        result = self.preprocessor.remove_html_tags(text)
        self.assertEqual(result, expected)

    def test_remove_emails(self):
        text = "Contact us at test@example.com for details."
        expected = "Contact us at  for details."
        result = self.preprocessor.remove_emails(text)
        self.assertEqual(result, expected)

    def test_normalize_unicode(self):
        text = "این یک متن است"
        normalized_text = self.preprocessor.normalize_unicode(text)
        self.assertEqual(normalized_text, text)

    def test_remove_cyrillic(self):
        text = "This is Cyrillic: Привет"
        expected = "This is Cyrillic: "
        result = self.preprocessor.remove_cyrillic(text)
        self.assertEqual(result, expected)

    def test_pre_process_alphabet_numbers(self):
        text = "۱۲۳۴ و abc"
        expected = "1234 و abc"
        result = self.preprocessor.pre_process_alphabet_numbers(text)
        self.assertEqual(result, expected)

    def test_handle_persian_punctuation(self):
        text = "سلام، جهان!"
        expected = "سلام  جهان "
        result = self.preprocessor.pre_process_signs(text)
        self.assertEqual(result, expected)

    def test_remove_english_words(self):
        text = "این متن شامل English است"
        expected = "این متن شامل است"
        result = self.preprocessor.remove_english_words(text)
        self.assertEqual(result, expected)

    def test_clean_extra_spaces(self):
        text = "این    یک  متن  است  "
        expected = "این یک متن است"
        result = self.preprocessor.clean_extra_spaces(text)
        self.assertEqual(result, expected)

    def test_remove_half_space(self):
        text = "این\u200C متن\u200C تست\u200C است"
        expected = "این متن تست است"
        result = self.preprocessor.remove_half_space(text)
        self.assertEqual(result, expected)

    def test_remove_numbers_only_cells(self):
        text = "12345"
        expected = ""
        result = self.preprocessor.remove_numbers_only_cells(text)
        self.assertEqual(result, expected)

    def test_handle_emojis(self):
        text = "این متن 😊 تست است"
        expected_remove = "این متن  تست است"
        expected_replace = "این متن [EMOJI] تست است"
        expected_sentiment = "این متن positive تست است"
        self.assertEqual(self.preprocessor.handle_emojis(text, "remove"), expected_remove)
        self.assertEqual(self.preprocessor.handle_emojis(text, "replace"), expected_replace)
        self.assertEqual(self.preprocessor.handle_emojis(text, "sentiment"), expected_sentiment)

    def test_convert_persian_to_standard_digits(self):
        text = "۱۲۳۴۵۶۷۸۹۰"
        expected = "1234567890"
        result = self.date_converter.convert_persian_to_standard_digits(text)
        self.assertEqual(result, expected)

    def test_handle_persian_dates(self):
        text = "تاریخ امروز ۱۴۰۲/۰۵/۲۰ است"
        expected = "تاریخ امروز 2023-08-11 است"
        result = self.date_converter.handle_persian_dates(text, convert_to_standard=True)
        self.assertEqual(result, expected)

    def test_process_text(self):
        column = ["این-یک متنُ شامل 😊 است"]
        expected = ["این یک متن شامل است"]
        result = self.preprocessor.process_text(column)
        self.assertEqual(result.tolist(), expected)

if __name__ == "__main__":
    unittest.main()


class TestPersianTextPreprocessor(unittest.TestCase):
    def setUp(self):
        self.preprocessor_default = PersianTextPreprocessor(task="default")
        self.preprocessor_translation = PersianTextPreprocessor(task="translation")
        self.preprocessor_sentiment = PersianTextPreprocessor(task="sentiment")
        self.preprocessor_ner = PersianTextPreprocessor(task="ner")
        self.preprocessor_topic_modeling = PersianTextPreprocessor(task="topic_modeling")
        self.preprocessor_spam_detection = PersianTextPreprocessor(task="spam_detection")
        self.preprocessor_summarization = PersianTextPreprocessor(task="summarization")
        self.date_converter = ConvertPersianDate()

    def test_remove_cyrillic(self):
        text = "این متن حاوی متن سیریلیک Привет است"
        expected = "این متن حاوی متن سیریلیک  است"
        result = self.preprocessor_default.remove_cyrillic(text)
        self.assertEqual(result, expected)

    def test_handle_persian_dates(self):
        text = "تاریخ امروز ۱۴۰۲/۰۵/۲۰ است"
        expected = "تاریخ امروز 2023-08-11 است"
        result = self.date_converter.handle_persian_dates(text, convert_to_standard=True)
        self.assertEqual(result, expected)

    def test_remove_english_words(self):
        text = "این یک متن شامل English کلمات است"
        expected = "این یک متن شامل کلمات است"
        result = self.preprocessor_default.remove_english_words(text)
        self.assertEqual(result, expected)

    def test_remove_url(self):
        text = "این یک متن است با لینک https://example.com و www.test.com"
        expected = "این یک متن است با لینک  و "
        result = self.preprocessor_default.remove_url(text)
        self.assertEqual(result, expected)

    def test_remove_html_tags(self):
        text = "این <b>متن</b> با تگ‌های <i>HTML</i> است"
        expected = "این متن با تگ‌های HTML است"
        result = self.preprocessor_default.remove_html_tags(text)
        self.assertEqual(result, expected)

    def test_clean_extra_spaces(self):
        text = "این     یک     متن    با     فاصله‌های اضافی    است"
        expected = "این یک متن با فاصله‌های اضافی است"
        result = self.preprocessor_default.clean_extra_spaces(text)
        self.assertEqual(result, expected)

    def test_process_text_default(self):
        column = ["این یک متن شامل 😊 و لینک https://example.com است."]
        expected = ["این یک متن شامل و لینک است"]
        result = self.preprocessor_default.process_text(column).tolist()
        self.assertEqual(result, expected)

    def test_process_text_translation(self):
        column = ["این یک متن ۱۴۰۲/۰۵/۲۰ شامل 😊 و لینک https://example.com است."]
        expected = ["این یک متن 2023-08-11 شامل 😊 و لینک است ."]
        result = self.preprocessor_translation.process_text(column).tolist()
        self.assertEqual(result, expected)

    def test_process_text_sentiment(self):
        column = ["این یک متن  شامل 😊 و لینک https://example.com است."]
        expected = ["این یک متن شامل positive و لینک است"]
        result = PersianTextPreprocessor(task="sentiment").process_text(column).tolist()
        self.assertEqual(result, expected)

    def test_process_text_ner(self):
        column = ["این یک متن  شامل 😊 و لینک https://example.com است."]
        expected = ["این یک متن شامل emoji و لینک است"]
        result = self.preprocessor_ner.process_text(column).tolist()
        self.assertEqual(result, expected)

    def test_process_text_topic_modeling(self):
        column = ["این یک متن  شامل 😊 و لینک https://example.com است."]
        expected = ["این یک متن شامل و لینک است"]
        result = self.preprocessor_topic_modeling.process_text(column).tolist()
        self.assertEqual(result, expected)

    def test_process_text_spam_detection(self):
        column = ["این یک متن  شامل 😊 و لینک https://example.com است."]
        expected = ["این یک متن شامل و لینک است"]
        result = self.preprocessor_spam_detection.process_text(column).tolist()
        self.assertEqual(result, expected)

    def test_process_text_summarization(self):
        column = ["این یک متن  شامل 😊 و لینک https://example.com است."]
        expected = ["این یک متن شامل و لینک است ."]
        result = self.preprocessor_summarization.process_text(column).tolist()
        self.assertEqual(result, expected)

    def test_handle_emojis_remove(self):
        text = "این یک متن 😊 تست است"
        expected = "این یک متن  تست است"
        result = self.preprocessor_default.handle_emojis(text, "remove")
        self.assertEqual(result, expected)

    def test_handle_emojis_replace(self):
        text = "این یک متن 😊 تست است"
        expected = "این یک متن [EMOJI] تست است"
        result = self.preprocessor_default.handle_emojis(text, "replace")
        self.assertEqual(result, expected)

    def test_handle_emojis_sentiment(self):
        text = "این یک متن 😊 تست است"
        expected = "این یک متن  positive  تست است"
        result = self.preprocessor_default.handle_emojis(text, "sentiment")
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()


class TestEnglishTextPreprocessor(unittest.TestCase):
    def setUp(self):
        self.preprocessor = EnglishTextPreprocessor()
        self.test_data = pd.Series([
            "Hello World! 😊 Check out https://example.com",
            "This is a test @user #hashtag",
            "I can't believe it's not butter!",
            "\u00e9 is the accented letter e.",
            "😂😂 Oh no! That's unfortunate."
        ])

    def test_to_lower_case(self):
        result = self.test_data.apply(self.preprocessor.to_lower_case)
        expected = pd.Series([
            "hello world! 😊 check out https://example.com",
            "this is a test @user #hashtag",
            "i can't believe it's not butter!",
            "\u00e9 is the accented letter e.",
            "😂😂 oh no! that's unfortunate."
        ])
        pd.testing.assert_series_equal(result, expected)

    def test_clean_text_percent_elements(self):
        input_text = "This %i%m %p is a test string."
        result = self.preprocessor.clean_text_percent_elements(input_text)
        expected = "This is a test string."
        self.assertEqual(result, expected)

    def test_apply_normalization(self):
        input_text = "\u00e9 is the accented letter e."  # Input with accented 'é'
        result = self.preprocessor.normalize_unicode(input_text)
        expected = "e is the accented letter e."
        self.assertEqual(result, expected)

    def test_correct_spelling(self):
        input_text = "wht is a tst sentnce."
        result = self.preprocessor.correct_spelling(input_text)
        expected = "what is a test sentence ."
        self.assertEqual(result, expected)

    def test_handle_emojis(self):
        input_text = "I am so happy 😊"
        result = self.preprocessor.handle_emojis(input_text, strategy="replace")
        expected = "I am so happy  EMOJI "
        self.assertEqual(result, expected)

    def test_remove_url_and_html(self):
        input_text = "Check this out: <b>bold</b> https://example.com"
        result = self.preprocessor.remove_url_and_html(input_text)
        expected = "Check this out: bold"
        self.assertEqual(result, expected)

    def test_remove_elements(self):
        input_text = "This is a test @user #hashtag"
        result = self.preprocessor.remove_elements(input_text)
        expected = "This is a test"
        self.assertEqual(result, expected)

    def test_clean_punctuation(self):
        input_text = "Hello, World! It's a test."
        result = self.preprocessor.clean_punctuation(input_text)
        expected = "Hello World Its a test"
        self.assertEqual(result, expected)

    def test_clean_extra_spaces(self):
        input_text = "This  is  a    test.\nNew line."
        result = self.preprocessor.clean_extra_spaces(input_text)
        expected = "This is a test. New line."
        self.assertEqual(result, expected)

    def test_remove_stopwords(self):
        tokens = ["this", "is", "a", "test"]
        result = self.preprocessor.remove_stopwords(tokens)
        expected = ["test"]
        self.assertEqual(result, expected)

    def test_apply_lemmatization(self):
        tokens = ["jumps", "faster", "worse", "arrived", "went", "tallest"]
        result = self.preprocessor.apply_lemmatization(tokens)
        expected = ["jump", "fast", "bad", "arrive", "go", "tall"]
        self.assertEqual(result, expected)

    def test_apply_stemming(self):
        tokens = ["jumps", "faster", "worse", "arrived", "went", "tallest"]
        result = self.preprocessor.apply_stemming(tokens)
        expected = ["jump", "fast", "bad", "arrive", "go", "tall"]
        self.assertEqual(result, expected)

    def test_process_column_default_task(self):
        result = self.preprocessor.process_column(self.test_data)
        expected = pd.Series([
            "hello world emoji check",
            "test",
            "believe butter",
            "e accent letter e",
            "emoji emoji oh unfortunate"
        ])
        pd.testing.assert_series_equal(result, expected)

    def test_process_column_translation_task(self):
        self.preprocessor = EnglishTextPreprocessor(task="translation")
        result = self.preprocessor.process_column(self.test_data)
        expected = pd.Series([
            "hello world ! 😊 check out",
            "this is a test",
            "i can not believe it is not butter !",
            "e is the accented letter e .",
            "😂😂 oh no ! that is unfortunate ."
        ])
        pd.testing.assert_series_equal(result, expected)

    def test_process_column_sentiment_task(self):
        self.preprocessor = EnglishTextPreprocessor(task="sentiment")
        result = self.preprocessor.process_column(self.test_data)
        expected = pd.Series([
            "hello world positive check out",
            "this be a test",
            "i can not believe it be not butter",
            "e be the accented letter e",
            "positive positive oh no that be unfortunate"
        ])
        pd.testing.assert_series_equal(result, expected)

    def test_process_column_ner_task(self):
        self.preprocessor = EnglishTextPreprocessor(task="ner")
        result = self.preprocessor.process_column(self.test_data)
        expected = pd.Series([
            "hello world ! check out",
            "this is a test",
            "i can not believe it is not butter !",
            "e is the accented letter e .",
            "oh no ! that is unfortunate ."
        ])
        pd.testing.assert_series_equal(result, expected)

    def test_process_column_topic_modeling_task(self):
        self.preprocessor = EnglishTextPreprocessor(task="topic_modeling")
        result = self.preprocessor.process_column(self.test_data)
        expected = pd.Series([
            "hello world check out",
            "this be a test",
            "i can not believe it be not butter",
            "e be the accented letter e",
            "oh no that be unfortunate"
        ])
        pd.testing.assert_series_equal(result, expected)

    def test_process_column_spam_detection_task(self):
        self.preprocessor = EnglishTextPreprocessor(task="spam_detection")
        result = self.preprocessor.process_column(self.test_data)
        expected = pd.Series([
            "hello world check out",
            "this is a test",
            "i can not believe it is not butter",
            "e is the accented letter e",
            "oh no that is unfortunate"
        ])
        pd.testing.assert_series_equal(result, expected)

    def test_process_column_summarization_task(self):
        self.preprocessor = EnglishTextPreprocessor(task="summarization")
        result = self.preprocessor.process_column(self.test_data)
        expected = pd.Series([
            "hello world check out",
            "this is a test",
            "i can not believe it is not butter",
            "e is the accented letter e",
            "oh no that is unfortunate"
        ])
        pd.testing.assert_series_equal(result, expected)


if __name__ == "__main__":
    unittest.main()
