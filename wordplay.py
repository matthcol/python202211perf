def isPalindrome(word: str) -> bool:
    """check if a word is a palindrome

    arguments:
    - word : word to check
    """
    return word == word[::-1]

# isPalindrome(121)
# isPalindrome([1,2,1])
isPalindrome("kayak")
