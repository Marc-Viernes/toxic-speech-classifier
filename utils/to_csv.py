import os
import csv
import re
import glob


def extract_text_from_file(file_path):
    """
    Extract text content from a file, removing the numbering format (x. text)
    """
    texts = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Split by lines and process each line
        lines = content.strip().split("\n")

        for line in lines:
            line = line.strip()
            if line:  # Skip empty lines
                # Remove numbering pattern (number followed by period and space)
                # This handles patterns like "1. ", "23. ", etc.
                cleaned_text = re.sub(r"^\d+\.\s*", "", line)
                if cleaned_text:  # Only add non-empty text
                    texts.append(cleaned_text)

    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

    return texts


def determine_label(filename):
    """
    Determine label based on filename
    Returns 1 if filename contains 'tel', 0 otherwise
    """
    filename_lower = filename.lower()
    if "tel" in filename_lower and "non_tel" not in filename_lower:
        return 1
    else:
        return 0


def convert_txt_to_csv(input_directory=".", output_file="output.csv"):
    """
    Convert all txt files in the directory to a single CSV file
    """
    # Find all txt files in the directory
    txt_files = glob.glob(os.path.join(input_directory, "*.txt"))

    if not txt_files:
        print("No txt files found in the directory!")
        return

    print(f"Found {len(txt_files)} txt files:")
    for file in txt_files:
        print(f"  - {os.path.basename(file)}")

    # Prepare data for CSV
    csv_data = []

    for file_path in txt_files:
        filename = os.path.basename(file_path)
        label = determine_label(filename)
        texts = extract_text_from_file(file_path)

        print(f"\nProcessing {filename}:")
        print(f"  Label: {label}")
        print(f"  Extracted {len(texts)} text entries")

        # Add each text entry with its label to the CSV data
        for text in texts:
            csv_data.append([text, label])

    # Write to CSV file
    try:
        with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            # Write header
            writer.writerow(["text", "label"])

            # Write data
            writer.writerows(csv_data)

        print(f"\nCSV file created successfully: {output_file}")
        print(f"Total entries: {len(csv_data)}")

        # Print summary
        tel_count = sum(1 for row in csv_data if row[1] == 1)
        non_tel_count = sum(1 for row in csv_data if row[1] == 0)
        print(f"TEL entries: {tel_count}")
        print(f"Non-TEL entries: {non_tel_count}")

    except Exception as e:
        print(f"Error writing CSV file: {e}")


def main():
    """
    Main function to run the conversion
    """
    print("TXT to CSV Converter")
    print("=" * 30)

    # You can modify these parameters as needed
    input_dir = (
        "./datasets/TEL/"  # Current directory, change if your txt files are elsewhere
    )
    output_csv = "converted_data.csv"  # Output CSV filename

    # Run the conversion
    convert_txt_to_csv(input_dir, output_csv)


if __name__ == "__main__":
    main()
