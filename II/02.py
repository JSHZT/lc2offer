class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret, count = '', 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or count:
            if i >= 0:
                count += ord(a[i]) - ord('0')
            if j >= 0:
                count += ord(b[j]) - ord('0')
            ret += str(count % 2)
            count //= 2
            i, j = i - 1, j - 1
        return ret[::-1]



if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary())