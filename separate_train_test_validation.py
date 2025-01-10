import pandas as pd
import argparse
from sklearn.model_selection import train_test_split

# Constants for default ratios and random state
DEFAULT_TRAIN_RATIO = 0.7
DEFAULT_VAL_RATIO = 0.2
DEFAULT_TEST_RATIO = 0.1
DEFAULT_RANDOM_STATE = 42


def load_csv(file_path):
    """Load the CSV file and return the DataFrame."""
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded data from {file_path}. Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        raise


def split_data(df, target_col, train_ratio, val_ratio, test_ratio, random_state):
    """Split the DataFrame into train, validation, and test sets."""
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found in the dataset.")

    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Split into train and temporary sets
    X_train_temp, X_test, y_train_temp, y_test = train_test_split(
        X, y, test_size=test_ratio, random_state=random_state
    )

    # Further split temporary set into train and validation
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_temp,
        y_train_temp,
        test_size=val_ratio / (train_ratio + val_ratio),
        random_state=random_state
    )

    return X_train, X_val, X_test, y_train, y_val, y_test


def save_to_csv(features, targets, filename):
    """Save features and targets as a single CSV file."""
    try:
        df = features.copy()
        df['target'] = targets
        df.to_csv(filename, index=False)
        print(f"Saved dataset to {filename}")
    except Exception as e:
        print(f"Error saving dataset to {filename}: {e}")


def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="Split preprocessed data into train, validation, and test sets.")
    parser.add_argument("--input", type=str, required=True,
                        help="Path to the preprocessed CSV file (output of main.py).")
    parser.add_argument("--target", type=str, required=True, help="Name of the target column in the dataset.")
    parser.add_argument("--train_ratio", type=float, default=DEFAULT_TRAIN_RATIO,
                        help="Train set ratio (default: 0.7).")
    parser.add_argument("--val_ratio", type=float, default=DEFAULT_VAL_RATIO,
                        help="Validation set ratio (default: 0.2).")
    parser.add_argument("--test_ratio", type=float, default=DEFAULT_TEST_RATIO, help="Test set ratio (default: 0.1).")
    parser.add_argument("--random_state", type=int, default=DEFAULT_RANDOM_STATE,
                        help="Random state for reproducibility.")
    parser.add_argument("--output_dir", type=str, default="Splits", help="Directory to save the output datasets.")
    args = parser.parse_args()

    try:
        # Load preprocessed data
        df = load_csv(args.input)

        # Split the data
        X_train, X_val, X_test, y_train, y_val, y_test = split_data(
            df, args.target, args.train_ratio, args.val_ratio, args.test_ratio, args.random_state
        )

        # Save splits to CSV
        save_to_csv(X_train, y_train, f"{args.output_dir}/train.csv")
        save_to_csv(X_val, y_val, f"{args.output_dir}/validation.csv")
        save_to_csv(X_test, y_test, f"{args.output_dir}/test.csv")

        print("Data splitting completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
