import sys

def solution(input_from_question):
    isbn = input_from_question.strip()

    total = sum((10 - i) * int(digit) for i, digit in enumerate(isbn[:-1]))

    if total % 11 == int(isbn[-1]) or (total % 11 == 0 and isbn[-1].upper() == 'X'):
        return "VALID"
    else:
        return "INVALID"

# Get input and print the output
input_from_question = input()
print(solution(input_from_question))
