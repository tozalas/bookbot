# A Python script to analyze the text of a book file.
# The script calculates the total number of words and the frequency of each character in the book.
# It then prints a formatted report with the results.

from stats import word_count, character_count, sorted_dict
import sys


def get_book_text(file_path):
    """
    Reads the content of a book file and returns the text.

    :param file_path: Path to the book file.
    :return: Text of the book or raises an error if the file cannot be read.
    """
    with open(file_path, 'r') as file:
        book_text = file.read()
    return book_text


def print_report(file_path, num_words, sorted_list):
    """
    Prints a formatted report of the word count and character frequencies.

    :param file_path: Path to the book file being analyzed.
    :param num_words: The total number of words in the book.
    :param sorted_list: A sorted list of dictionaries containing character counts.
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def main():
    """
    Main function to handle input, process the book text, and generate the report.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_file_path = sys.argv[1]  # Path to the book file provided as a command-line argument
    book_text = get_book_text(book_file_path)  # Read the book text

    num_words = word_count(book_text)  # Calculate the total number of words
    
    char_count = character_count(book_text)  # Calculate the frequency of each character
    sorted_list = sorted_dict(char_count)  # Sort the character counts by character

    print_report(book_file_path, num_words, sorted_list)  # Print the analysis report


if __name__ == "__main__":
    main()