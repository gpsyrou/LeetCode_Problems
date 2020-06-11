'''
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

'''
class Solution(object):
    def selfDividingNumbers(self, left, right):
        ls = []
        for number in range(left, right + 1):
            num_s = str(number)
            if '0' in num_s:
                continue
            else:
                flag = 0
                for digit in num_s:
                    if (number%int(digit) == 0):
                        flag+=1
                if (flag == len(num_s)):
                    ls.append(number)
                    
        return ls
