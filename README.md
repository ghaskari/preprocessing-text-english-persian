# English and Persian Text Preprocessing Pipeline

This project provides a robust preprocessing pipeline for English and Persian text, designed for a variety of Natural Language Processing (NLP) tasks such as translation, sentiment analysis, named entity recognition (NER), and more. It includes tools for data cleaning, normalization, frequency analysis, and dataset preparation for machine learning models.

---

## Features

- **Task-Specific Preprocessing**:
  - Supports tasks like `translation`, `sentiment`, `ner`, `spam_detection`, `topic_modeling`, and `summarization`.
- **Language-Specific Preprocessing**:
  - Persian: Diacritic removal, numeral normalization, punctuation handling.
  - English: Spelling correction, contractions expansion, lemmatization.
- **Dataset Splitting**:
  - Splits data into train, validation, and test sets with configurable ratios.
- **Frequency Analysis**:
  - Word and character frequency analysis with export to CSV and Excel files.

---

## Prerequisites

### Python Version
- Requires Python 3.8 or higher.

### Install Dependencies
Install required libraries:
```bash
pip install -r requirements.txt
```
Download the SpaCy model for English processing:
```bash
python -m spacy download en_core_web_sm
```

---

## Usage

### Step 1: Preprocess Data
Run the `main.py` script to preprocess data for a specific task. Example for the **translation task**:
```bash
python main.py --task translation --input translation_data.csv --output output_directory
```

#### Arguments:
- `--task`: The NLP task (`translation`, `sentiment`, `ner`, etc.).
- `--input`: Path to the input CSV file.
- `--output`: Directory to save the cleaned data.

---

### Step 2: Split Dataset (Optional)
Use `separate_train_test_validation.py` to split the preprocessed dataset into train, validation, and test sets:
```bash
python separate_train_test_validation.py \
  --input output_directory/cleaned_data_translation.csv \
  --target Persian \
  --train_ratio 0.7 \
  --val_ratio 0.2 \
  --test_ratio 0.1 \
  --output_dir output_directory
```

#### Arguments:
- `--input`: Path to the preprocessed file.
- `--target`: The target column (e.g., `Persian` for translation).
- `--train_ratio`, `--val_ratio`, `--test_ratio`: Ratios for dataset splitting.
- `--output_dir`: Directory to save the train/val/test splits.

---

### Step 3: Frequency Analysis (Optional)
Analyze word and character frequencies using `character_word_count.py`:
```python
from character_word_count import WordCharacterCount

# Example dataset
data = ["Hello world!", "Welcome to preprocessing."]

# Initialize the tool
counter = WordCharacterCount(output_directory="output_directory")

# Generate word frequency report
word_freq = counter.word_count(data, file_name="example_word_frequency")

# Generate character frequency report
char_freq = counter.character_count(data, file_name="example_char_frequency")
```

---

## Project Structure

After running the scripts, the directory structure will look like this:

```plaintext
.
├── main.py                     # Main preprocessing script.
├── english_text_preprocessor.py # English-specific preprocessing utilities.
├── persian_text_preprocessor.py # Persian-specific preprocessing utilities.
├── Dictionaries_En.py          # English dictionaries and mappings.
├── Dictionaries_Fa.py          # Persian dictionaries and mappings.
├── character_word_count.py     # Word and character frequency analysis tool.
├── separate_train_test_validation.py # Dataset splitting script.
├── stopwords.txt               # Persian stopword list.
├── requirements.txt            # Dependencies list.
├── translation_data.csv        # Sample input dataset.
├── output_directory/           # Directory containing generated outputs.
│   ├── cleaned_data_translation.csv   # Cleaned dataset (CSV format).
│   ├── cleaned_data_translation.xlsx  # Cleaned dataset (Excel format).
│   ├── train.csv                       # Training set.
│   ├── validation.csv                  # Validation set.
│   ├── test.csv                        # Test set.
│   ├── example_word_frequency_WordsCount.csv    # Word frequency report (CSV).
│   ├── example_char_frequency_CharactersCount.csv # Character frequency report (CSV).
├── README.md                   # Project documentation.
```

---

## Supported Tasks

1. **Translation**:
   - Processes datasets with `English` and `Persian` columns.
   - Retains minimal normalization to preserve translation context.

2. **Sentiment Analysis**:
   - Cleans data by removing emojis, punctuation, and stopwords.

3. **Named Entity Recognition (NER)**:
   - Retains entity-specific context while applying basic normalization.

4. **Topic Modeling**:
   - Removes stopwords and applies lemmatization for better topic clustering.

5. **Spam Detection**:
   - Prepares datasets for binary spam vs. non-spam classification.

6. **Summarization**:
   - Retains sentence structure and punctuation for summary generation.

7. **Default Task**:
   - Applies general-purpose text cleaning and normalization.

---

## Sample Input and Output

### Input: `translation_data.csv`
```csv
English,Persian
"Hello, world!", "سلام دنیا!"
"This is an example.", "این یک مثال است."
```

### Preprocessed Output
Saved in `output_directory/cleaned_data_translation.csv`:
```csv
English,Persian
"hello world", "سلام دنیا"
"this is an example", "این یک مثال است"
```

### Dataset Splits
Saved in `output_directory/`:
- `train.csv`
- `validation.csv`
- `test.csv`

---

## Customization

### Task Configurations
- Modify preprocessing settings in `english_text_preprocessor.py` and `persian_text_preprocessor.py`.
- Adjust configurations for punctuation, stopword removal, or specific tasks.

---