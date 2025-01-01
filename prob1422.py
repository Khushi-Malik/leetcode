"""Maximum Score After Splitting a String"""

def maxScore(s: str) -> int:
    """ Given a string s of zeros and ones, return the maximum score after splitting 
    the string into two non-empty substrings (i.e. left substring and right substring).
    The score after splitting a string is the number of zeros in the left substring 
    plus the number of ones in the right substring.

    >>> maxScore("011101")
    5
    """
    # NOT VERY EFFICIENT
    # possible = []

    # for i in range(1, len(s)):
    #     left = s[:i]
    #     right = s[i:]

    #     zeroes = left.count("0")
    #     ones = right.count("1")

    #     possible.append(zeroes+ones)
    
    # return max(possible)

    #BEST SOLUTION
    # ones = 0
    # zeros = 0
    # best = float('-inf')

    # for i in range(len(s) - 1):
    #     if s[i] == "1":
    #         ones += 1
    #     else:
    #         zeros += 1
        
    #     best = max(best, zeros - ones)
        
    # if s[-1] == "1":
    #     ones += 1
    
    # return best + ones

    #ANOTHER SOLUTION
    ones = s.count("1")
    zeros = 0
    ans = 0 

    for i in range(len(s) - 1):
        if s[i] == "1":
            ones -= 1
        else:
            zeros += 1
    
        ans = max(ans, zeros + ones)
    
    return ans


print(maxScore("1111"))