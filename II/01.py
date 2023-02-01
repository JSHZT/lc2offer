class Solution:
    def divide(self, a: int, b: int) -> int:
        result = 0
        sign = 1 if (a > 0 and b > 0) or (a < 0 and b < 0) else -1
        a, b = abs(a), abs(b)
        while a >= b:
            cnt, a_ = self.get_cnt(a, b)
            a -= a_
            result += cnt
        result = result * sign
        return  result -1 if result >= 2**31 else result

    def get_cnt(self, x, y):
        n = 1
        while x > y << 1:
            y <<= 1
            n <<= 1
        return n, y
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.divide(-15, 2))
