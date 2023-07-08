def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    # for index, letter in enumerate(word):
    #     if letter != word[len(word) - index - 1]:
    #         return False

    for index in range(len(word)//2):
        if word[index] != word[-index - 1]:
            return False

    return True
