from wordplay import isPalindrome

def testIsPalindromeOk():
    assert isPalindrome("kayak")

def testIsPalindromeKo():
    assert not isPalindrome("canoë")