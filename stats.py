def word_counter(book_text):
    counter = 0
    words = book_text.split()

    for word in words:
        counter += 1

    return counter

def char_counter(book_text):
    char_dict = {}
    book_text_lower = book_text.lower()

    for char in book_text_lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    return char_dict