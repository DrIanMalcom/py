def isPalindrome(x: int) -> bool:

    numToStr = str(x)

    return numToStr[::-1] == numToStr
