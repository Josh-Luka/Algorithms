from collections import Counter

# some source help from Module 4 slides from lecture 2 & 3 as well as source code from Module 4


def countPermStr(mainStr, compStr):

    mx = len(mainStr)
    cx = len(compStr)
    mCount = Counter(mainStr[:cx])
    cCount = Counter(compStr)
    matchNum = 0

    if len(compStr) == 0:
        raise ValueError("String 2 is Empty")
    if mainStr is None or compStr is None:
        raise ValueError("One of the Strings is Empty")
    if len(compStr) > len(mainStr):
        raise ValueError("Second String Must not be Longer Than First String")
    
    if mCount == cCount:
        matchNum += 1

    for x in range(cx, mx):
        mCount[mainStr[x]] = mCount[mainStr[x]] + 1
        z = mainStr[x - cx]
        mCount[z] = mCount[z] - 1

        if mCount[z] == 0:
            del mCount[z]
        if mCount == cCount:
            matchNum += 1
    return matchNum
