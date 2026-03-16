from typing import List

# Solution 2 - 100% runtime and 99.97% memory
class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for char in path.split("/"):
            if char == "..":
                if res:
                    res.pop()
            elif char and char!=".":
                    res.append(char)
        return "/"+"/".join(res)

# Solution 1 - 200% runtime and 89% memory
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_marker = "/"
        res = []
        for char in path.split("/"):
            if char:
                if char == "..":
                    if res:
                        res.pop()
                elif char == ".":
                    continue
                else:
                    res.append(char)
        return path_marker+"/".join(res)

# path = "/neetcode/practice//...///../courses"
# expected= "/neetcode/practice/courses"

# path = "/..//"
# expected= "/"

# path="/home//foo/"
# expected = "/home/foo"

# path = "/..//_home/a/b/..///"
# expected= "/_home/a"