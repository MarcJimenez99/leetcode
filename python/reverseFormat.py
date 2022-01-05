class Solution(object):
    def reverseFormat(self, s):
        if len(s) != 11:
            print("Invalid String")
            return "Invalid String"
        if s[2] and s[6] != "-":
            print("Invalid String")
            return "Invalid String"
        for letter in s:
            #USE REGEX BUT DAMN I DONT KNOW THEM

def main():

    s = "12-345-6789"

    result = Solution()
    result.reverseFormat(s)
if __name__ = "__main__":
    main()