'''
1678. Goal Parser Interpretation

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
'''
class Solution:
    def interpret(self, command: str) -> str:
        final = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                final.append("G")
                i += 1
            else:
                if command[i] + command[i+1] == "()":
                    final.append("o")
                    i += 2
                else:
                    final.append("al")
                    i += 4
        return ''.join([x for x in final])