def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if len(word) == 1:
        return True
    if len(word) == 2 and word[0] == word[1]:
        return True
    else:
        word_lower = word.lower()
        first_letter = word_lower[low_index]
        last_letter = word_lower[high_index]
        if first_letter != last_letter:
            return False
        else:
            new_word = word_lower[1:-1]
            return is_palindrome_recursive(new_word, 0, len(new_word) - 1)
