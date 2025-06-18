def word_count(text):
    """
    Counts the number of words in the given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)


def character_count(text):
    """
    Counts the frequency of each character in the given text.

    Args:
        text (str): The text to count characters in.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_count = {}
    for char in text:
        char = char.lower()  # Normalize to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(dict):
    """
    Helper function to extract the value for sorting.

    Args:
        dict (dict): A dictionary with keys "char" and "num".

    Returns:
        int: The value associated with the "num" key.
    """
    return dict["num"]


def sorted_dict(dict):
    """
    Sorts a dictionary by the frequency of alphabetic characters in descending order.

    Args:
        dict (dict): The dictionary to sort, with characters as keys and their counts as values.

    Returns:
        list: A sorted list of dictionaries in the format {"char": str, "num": int}, 
              containing only alphabetic characters.
    """
    sorted_dict = []
    for key in dict:
        if key.isalpha():  # Only include alphabetic characters
            sorted_dict.append({"char": key, "num": dict[key]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict
