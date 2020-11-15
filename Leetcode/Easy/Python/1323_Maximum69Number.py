'''
1323. Maximum 69 Number

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

'''
class Solution:
    def maximum69Number (self, num: int) -> int:
        max_num = num
        num_as_str = str(num)
        for i in range(len(num_as_str)):
            num_str = list(num_as_str)
            if num_str[i] == '6':
                num_str[i] = '9'
            else:
                num_str[i] = '6'
            print(num_str)
            temp = int(''.join(num_str))
            if  temp> max_num:
                max_num = int(temp)
        return max_num