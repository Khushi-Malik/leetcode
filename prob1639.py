"""1639. Number of Ways to Form a Target String Given a Dictionary"""

def numWays(words: list[str], target: str) -> int:
    numways = 0
    tarI = 0
    lenMax = len(words[0])
    k = 0
    while k < lenMax:
        maxI = k
        for i in range(maxI, lenMax):
            for word in words:
                if tarI < len(target) and word[i] == target[tarI]:
                    tarI += 1
                    if tarI == len(target):
                        tarI = 0
                        numways += 1
        k += 1
    return numways


print(numWays(["acca","bbbb","caca"], "aba"))
print(numWays(["abba","baab"], "bab"))
