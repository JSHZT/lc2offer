# 刷穿剑指offer II 
# T1.整数除法
## 题目描述

给定两个整数 `a` 和 `b` ，求它们的除法的商 `a/b` ，要求不得使用乘号 `'*'`、除号 `'/'` 以及求余符号 `'%'` 。

注意：

整数除法的结果应当截去 `（truncate）`其小数部分，例如：`truncate(8.345) = 8` 以及 `truncate(-2.7335) = -2`
假设我们的环境只能存储 32 位有符号整数，其数值范围是 `[−2^31, 2^31−1]`。本题中，如果除法结果溢出，则返回 `2^31 − 1`

## 输入输出示例
    输入：a = 15, b = 2
    输出：7
    解释：15/2 = truncate(7.5) = 7

    输入：a = 7, b = -3
    输出：-2
    解释：7/-3 = truncate(-2.33333..) = -2

## 题目解析
本道题规定不允许使用乘除余运算，最简单直接的想法是减法，被除数循环减去除数并统计减法次数，直到被除数再减去除数的结果小于0，减法次数即为答案。但假如被除数和除数都分别在两个极端,eg.a=2^31, b=1,则需要做2^31次减法，这样的时间复杂度是不允许的。

因此矛盾转化成减少减法的次数，关键是每次减去的数字要尽可能小，由此可以想到倍数计算，在不使用乘法的情况下只能使用位运算。

关键步骤算法流程如下：

* 循环将除数左移一位，并统计倍数，同样也能使用1左移1位进行，直到左移后大于被除数，则不进行左移操作
* 被除数减去放大的倍数后，循环上述操作，直到被除数小于除数

所累计的倍数就是答案

需要注意的细节是溢出问题，这里直接看代码即可

```python
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
```
---
# T2.二进制加法
## 题目描述

给定两个 01 字符串 `a` 和 `b `，请计算它们的和，并以二进制字符串的形式输出。
输入为 `非空` 字符串且`只包含数字 1 和 0`。


## 输入输出示例
    输入: a = "11", b = "10"
    输出: "101"

    输入: a = "1010", b = "1011"
    输出: "10101"

## 题目解析
思路直接，满二进一即可
```python
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

```