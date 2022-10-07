class Solution:
    def isPalindrome(self, x: int) -> str:
        if -2147483648 <= x <= 2147483648:
            x = list(str(x))
            rev_x = []
            for i in range(len(x)):
                rev_x.append(x[-(i + 1)])
            if rev_x == x:
                return 'true'
            else:
                return 'false'
        else:
            exit()
