'''The goal of this exercise is to convert a string to a new string where each character in the new string
is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.'''

def duplicate_encode(word):
    ok=''
    solution=[]
    result = ''
    box=[i.lower() for i in word]
    result = [box.count(i) for i in box]
    for i in result:
        if i == 1:
            solution.append('(')
        else:
            solution.append(')')
    for i in solution:
        ok+=i
    return ok
