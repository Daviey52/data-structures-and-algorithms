from pickletools import string1


class Brackets:
    def __init__(self):
        pass

    def validating_brackets(self, string1):
        self.string1 = string1
        stack = []
        pchar = {"(": ")", "{": "}", "[": "]"}
        for parenthese in string1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0



