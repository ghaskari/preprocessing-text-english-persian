import pandas as pd
from sklearn.model_selection import train_test_split

# Constants
DATA_FILE = 'DataSource/cleaned_OpenSubtitles-fa.csv'
TARGET_COL = 'target_column'  # Replace with your actual target column name
TRAIN_RATIO = 0.7
VAL_RATIO = 0.2
TEST_RATIO = 0.1
RANDOM_STATE = 42


def load_and_preprocess_data(file_path):
    """Load CSV file and preprocess data."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        raise


def split_train_val_test(df, train_ratio=TRAIN_RATIO, val_ratio=VAL_RATIO, test_ratio=TEST_RATIO,
                         random_state=RANDOM_STATE):
    """Split data into train, validation, and test sets."""
    X = df.drop(TARGET_COL, axis=1)
    y = df[TARGET_COL]

    X_train_temp, X_test_temp, y_train_temp, y_test_temp = train_test_split(
        X, y, test_size=test_ratio, random_state=random_state
    )

    X_train, X_val_temp, y_train, y_val_temp = train_test_split(
        X_train_temp,
        y_train_temp,
        test_size=(val_ratio + test_ratio) / (1 - train_ratio),
        random_state=random_state
    )

    # Final split: Remove test samples from temp set to get final test set
    X_val, X_test, y_val, y_test = train_test_split(
        X_val_temp,
        y_val_temp,
        test_size=test_ratio / (val_ratio + test_ratio),
        random_state=random_state
    )

    return X_train, X_val, X_test, y_train, y_val, y_test


def save_dataset(df, filename):
    """Save DataFrame to CSV file."""
    try:
        df.to_csv(filename, index=False)
        print(f"Dataset saved to {filename}")
    except Exception as e:
        print(f"Error saving dataset: {e}")


# Main execution
if __name__ == "__main__":
    try:
        # Load and preprocess data
        df = load_and_preprocess_data(DATA_FILE)

        # Split data into train, validation, and test sets
        X_train, X_val, X_test, y_train, y_val, y_test = split_train_val_test(df)

        # Save datasets
        train_data = pd.DataFrame({'features': X_train, 'target': y_train})
        val_data = pd.DataFrame({'features': X_val, 'target': y_val})
        test_data = pd.DataFrame({'features': X_test, 'target': y_test})

        save_dataset(train_data, 'train.csv')
        save_dataset(val_data, 'validation.csv')
        save_dataset(test_data, 'test.csv')

        print("Data splitting completed successfully.")

    except Exception as e:
        print(f"An error occurred during data splitting: {e}")
