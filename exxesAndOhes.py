'''Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.'''

def XO(string):
   #convert string into lowercase
    lowerString = string.lower()
    #use list comprehension to create lists of 'x' and 'o'
    exes=[i for i in lowerString if i == 'x']
    ohes=[i for i in lowerString if i == 'o']
    #compare the lengths of the two lists
    return len(exes) == len(ohes)
