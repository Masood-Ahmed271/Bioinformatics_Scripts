'''
Description: Assignment 3 Question 8 -> Given a collection of at most 10 symbols defining an ordered alphabet,
                                        and a positive integer n (n≤10).
                                        Return all strings of length n that can be formed from the alphabet,
                                        ordered lexicographically
Author: Masood Ahmed
UID: 3035812127

'''
# importing itertools to get repeated permutations
import itertools

'''
Description: this function finds permutations of the strings with k characters
parameters: listOfChar --> a list of all the characters
           k --> the length of each permutation

return:  a list of all the possible permutations
'''
def finding_permutations(listOfChar,k):
    final = []
    for p in itertools.product(listOfChar, repeat=k):
        p = ''.join(p)
        final.append(p)

    final.sort()
    return final

# main program area
if __name__ == "__main__":
    # Assuming that input is in the following form:
    # A C G T
    # 2

    inputFile = open('input.txt', 'r')
    lines = []
    for line in inputFile.readlines():
        line = line.rstrip('\n')
        lines.append(line)
    
    listOfChar = lines[0].split(" ")
    k = int(lines[-1])
    inputFile.close()
    result = finding_permutations(listOfChar,k)
    outputfile = open('outputQ8.txt', 'w')
    for each in result:
        outputfile.write(each + '\n')
    outputfile.close()
