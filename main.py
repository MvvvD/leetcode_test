from typing import List


def romanToInt(s: str) -> int:
    s = s.replace("IV", "IIII").replace('IX', "VIIII").replace('XL', 'XXXX').replace("XC", 'LXXXX'). \
        replace('CD', 'CCCC').replace("CM", 'DCCCC')
    result = 0
    d = {"I": '1', "V": '5', "X": '10', "L": "50", 'C': "100", "D": '500', "M": '1000'}
    for char in s:
        result += int(d[char])
    return result

    # https://leetcode.com/problems/roman-to-integer/submissions/
    # Runtime: 59 ms, faster than 76.40% of Python3 online submissions for Roman to Integer.
    # Memory Usage: 13.9 MB, less than 76.28% of Python3 online submissions for Roman to Integer.


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    strs.sort(key=len)
    res = strs[0]
    for i, j in enumerate(res):
        for s in strs[1:]:
            if s[i] != j:
                return res[:i]
    return res

    # https://leetcode.com/problems/longest-common-prefix/submissions/
    # Runtime: 62 ms, faster than 30.38% of Python3 online submissions for Longest Common Prefix.
    # Memory Usage: 13.8 MB, less than 88.10% of Python3 online submissions for Longest Common Prefix.


def isValid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False
    temp = []
    test = 0
    for ss in s:
        try:
            if ss == '(' or ss == '[' or ss == '{':
                temp.append(ss)
                test += 1

            elif temp[-1] == '(' and ss == ')' or temp[-1] == '[' and ss == ']' or temp[-1] == '{' and ss == '}':
                test -= 1
                temp.pop()
            else:
                return False
        except IndexError:
            return False
    return test == 0

    # https://leetcode.com/problems/valid-parentheses/submissions/
    # Runtime: 41 ms, faster than 69.87% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 13.9 MB, less than 69.91% of Python3 online submissions for Valid Parentheses.


def removeDuplicates(nums: List[int]) -> int:
    v = ""
    r = 0
    for n in nums:
        if v != n:
            v = n
            nums[r] = n
            r += 1
    return r

    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
    # Runtime: 82 ms, faster than 98.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # Memory Usage: 15.5 MB, less than 96.19% of Python3 online submissions for Remove Duplicates from Sorted Array.


def mySqrt(x: int) -> int:
    return int(x ** (1 / 2))

    # https://leetcode.com/problems/sqrtx/submissions/
    # Runtime: 26 ms, faster than 99.74% of Python3 online submissions for Sqrt(x).
    # Memory Usage: 13.8 MB, less than 96.24% of Python3 online submissions for Sqrt(x).


def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split(" ")[-1])

    # https://leetcode.com/problems/length-of-last-word/submissions/
    # Runtime: 22 ms, faster than 99.69% of Python3 online submissions for Length of Last Word.
    # Memory Usage: 13.9 MB, less than 79.87% of Python3 online submissions for Length of Last Word.


def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    h = haystack.split(needle)
    return len(h[0])

    # https://leetcode.com/problems/implement-strstr/submissions/
    # Runtime: 28 ms, faster than 96.90% of Python3 online submissions for Implement strStr().
    # Memory Usage: 13.8 MB, less than 97.15% of Python3 online submissions for Implement strStr().


def reverseBits(n: int) -> int:
    return int(str(format(n, '032b'))[::-1], 2)

    # https://leetcode.com/problems/reverse-bits/submissions/
    # Runtime: 31 ms, faster than 96.60% of Python3 online submissions for Reverse Bits.
    # Memory Usage: 13.8 MB, less than 94.29% of Python3 online submissions for Reverse Bits.
