# Solution 4 - 100% runtime and 84.02% memory
# Recursion-based solution
class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        def decode(index: int) -> int:
            temp = []
            num = 0
            while index < n:
                if s[index].isdigit():
                    num = num*10 + int(s[index])
                elif s[index]=="[":
                    output, index = decode(index + 1)
                    temp.extend(output*num)
                    num=0
                elif s[index]=="]":
                    return temp, index
                else:
                    temp.append(s[index])
                index += 1
            return temp, index

        return "".join(decode(0)[0])

# Solution 3 - 100% runtime and 100% memory
# Stack based solution
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != "]":
                stack.append(i)
            else:
                word = ""
                while stack and stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()

                k=""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*word)
        return ''.join(stack)

# Solution 2 - 100% runtime and 84.04% memory
# Recursion-based solution
class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        def decode(index: int, freq: int) -> int:
            temp =[]
            while index < n and s[index] != "]":
                if s[index].isdigit():
                    j = index
                    while s[j + 1].isdigit():
                        j += 1
                    # if multiplier has more than one char, take that as freq, skip to after "["
                    output, index = decode(j + 2, int(s[index:j + 1])) if index != j else decode(index + 2, int(s[index]))
                    temp += output
                else:
                    temp.append(s[index])
                index += 1
            return temp*freq, index
        return "".join(decode(0, 1)[0])

# Solution 1 - 65.39% runtime and 84.04% memory
# Recursion-based solution
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n=len(s)
        def decode(index: int, freq:int) -> int:
            start = index
            for _ in range(freq):
                index = start
                while index<n and s[index]!="]":
                    if s[index].isdigit():
                        j = index
                        while s[j + 1].isdigit():
                            j += 1
                        if index != j:
                            index = decode(j + 2, int(s[index:j+1]))
                        else:
                            index = decode(index + 2, int(s[index]))
                    else:
                        stack.append(s[index])
                    index+=1
            return index
        decode(0,1)
        return "".join(stack)

# s="3[a10[b]]"
# expected="abbbbbbbbbbabbbbbbbbbbabbbbbbbbbb"

# s = "2[a3[b]]c"
# expected = "abbbabbbc"

# s="2[a3[b]c]"
# expected = "abbbcabbbc"

# s = "axb3[z]4[c]"
# expected = "axbzzzcccc"

# s = "ab2[c]3[d]1[x]"
# expected = "abccdddx"