"""
Given a positive integer num, return the sum of its digits.

Bonus: Can you do it without using strings?

This includes print testing.

"""

def solve(num):
    tot = 0
    while num:
        tot += num % 10
        print(f"{tot}[tot] = {num}[num] %10")
        num //= 10
        print(f"{num} after {num}//10")

    print(f"final output = {tot}")


solve(123)

"""
explanation:

first, we find the last number by finding the remainder when divided by 10.
second, we divide that number by 10 to get the next "num" to iterate over

num = 123
1st iteration: tot = 0 + 3 = 3, num-->12
2nd iteration: tot = 3 + 2 = 5, num-->1
3rd iteration: tot = 5 + 1 = 6, num-->0
"""
