# Sum of Pairs

# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]

# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]

# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)

# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]



def sum_pairs(ints, s):
    validPairs = []
    solutionPair = []
    for i, j in enumerate(ints):
        for k in ints[i+1:]:
            if k + j == s: 
                validPairs.append([j,i,k, (len(ints)-1)-(ints[::-1].index(k))])
    if len(validPairs) == 0:
            return None
    elif len(validPairs) >= 2:
        distance = abs(validPairs[0][1] - validPairs[0][3])
        solutionIndex = 0
        for i in validPairs[::]:
            if abs(i[1] - i[3]) < distance:
                distance = abs(i[1] - i[3])
                solutionIndex += validPairs.index(i)
        solutionPair.append(validPairs[solutionIndex][0])
        solutionPair.append(validPairs[solutionIndex][2])
    else:
        solutionPair.append(validPairs[0][0])
        solutionPair.append(validPairs[0][2])
    return solutionPair
