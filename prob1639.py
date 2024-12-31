"""1639. Number of Ways to Form a Target String Given a Dictionary"""

def numWays(words: list[str], target: str) -> int:
    """My sol try"""
    # numways = 0
    # tarI = 0
    # lenMax = len(words[0])
    # k = 0
    # while k < lenMax:
    #     maxI = k
    #     for i in range(maxI, lenMax):
    #         for word in words:
    #             if tarI < len(target) and word[i] == target[tarI]:
    #                 tarI += 1
    #                 if tarI == len(target):
    #                     tarI = 0
    #                     numways += 1
    #     k += 1
    # return numways

    """A bit corrected"""
    # def helper(col, tarI):
    #     if tarI == len(target):  # Completed forming the target
    #         return 1
    #     if col == len(words[0]):  # Ran out of columns
    #         return 0

    #     # Count occurrences of target[tarI] in the current column
    #     count = 0
    #     for word in words:
    #         if word[col] == target[tarI]:
    #             count += 1

    #     # Either use the current column or skip it
    #     use_col = count * helper(col + 1, tarI + 1)  # Use this column for target[tarI]
    #     skip_col = helper(col + 1, tarI)  # Skip this column

    #     return use_col + skip_col

    # return helper(0, 0)

    """Correct solution using dynamic programming"""
    MOD = 10**9 + 7
    lenMax = len(words[0])
    target_len = len(target)
    
    # Precompute frequencies of each character in each column
    freq = [{} for _ in range(lenMax)]
    for word in words:
        for j, char in enumerate(word):
            if char not in freq[j]:
                freq[j][char] = 0
            freq[j][char] += 1

    # Initialize a dp array: dp[i] is the number of ways to form target[:i]
    dp = [0] * (target_len + 1)
    dp[0] = 1  # There's one way to form an empty target string

    # Iterate through each column
    for col in range(lenMax):
        for i in range(target_len - 1, -1, -1):  # Traverse target in reverse
            char = target[i]
            if char in freq[col]:
                dp[i + 1] = (dp[i + 1] + dp[i] * freq[col][char]) % MOD

    return dp[target_len]



print(numWays(["acca","bbbb","caca"], "aba"))
print(numWays(["abba","baab"], "bab"))
