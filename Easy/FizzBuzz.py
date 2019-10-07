'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        numbers = [x for x in range(1, n+1)]
        
        for indx, num in enumerate(numbers):

            if (num%3 == 0) and (num%5 == 0):
                numbers[indx] = 'FizzBuzz'
                continue
            elif num%3 == 0:
                numbers[indx] = 'Fizz'
            elif num%5 == 0:
                numbers[indx] = 'Buzz'
            else:
                numbers[indx] = str(num)
                
        return numbers
        
