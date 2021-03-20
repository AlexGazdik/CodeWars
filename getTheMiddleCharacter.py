'''You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.'''

def get_middle(s):
    count=0
    for i in s:
        count+=1
    mid=count//2
    if count % 2==0:
        return s[mid-1: mid+1]
    else:
        return s[mid]
