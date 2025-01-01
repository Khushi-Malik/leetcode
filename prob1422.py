"""Maximum Score After Splitting a String"""

def maxScore(s: str) -> int:
    """ Given a string s of zeros and ones, return the maximum score after splitting 
    the string into two non-empty substrings (i.e. left substring and right substring).
    The score after splitting a string is the number of zeros in the left substring 
    plus the number of ones in the right substring.

    >>> maxScore("011101")
    5
    """
    possible = []

    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]

        zeroes = left.count("0")
        ones = right.count("1")

        possible.append(zeroes+ones)
    
    return max(possible)


print(maxScore("011101"))