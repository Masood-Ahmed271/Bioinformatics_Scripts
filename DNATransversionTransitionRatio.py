'''
Description: Assignment 3 Question 7 -> Finding The transition/transversion ratio R(s1, s2) accurate to 2.dp given 
                                        two DNA strings s1 and s2 of equal length
Author: Masood Ahmed
UID: 3035812127

'''



'''
A function to just calculate the ratio and to round off to 2 decimal places
parameters: transitions --> number of transition
           transversions --> number of transversions
Return: ratio of transition/transversion

'''
def ratio(transitions,transversions):

    return round(transitions/transversions, 2)


'''
The function counting the transitions and transversions
parameters: s_1 --> String 1
           s_2 --> String 2
Return: ratio of transition/transversion

'''
def calculate_transition_transversion_ratio(s_1,s_2):

    typesOfTransitions = [('A', 'G'), ('C', 'T'), ('G', 'A'),  ('T', 'C')]
    transitions = 0
    transversions = 0

    for i in range(len(s_1)):
        if s_1[i] != s_2[i]:
            if (s_1[i],s_2[i]) not in typesOfTransitions:
                transversions += 1
            else:
                transitions += 1
    
    return ratio(float(transitions),float(transversions))


# mainFunction
if __name__ == "__main__":
    # Assuming that input is in the following form:
        # >string1
        # GCAACGCACAACGAAAACCCTTAGGGA
        # >string2
        # TTATCTGACAAAGAAAGCCGTCAACGG

    inputFile = open('input.txt', 'r')
    lines = []
    for line in inputFile.readlines():
        line = line.rstrip('\n')
        lines.append(line)

    string2 = lines.index(">string2")
    s_1 = ''.join(lines[1:string2]).upper()
    s_2 = ''.join(lines[string2+1:]).upper()
    inputFile.close()

    if len(s_1) != len(s_2):
        print("Can't calculate transition/transversion ratio as lengths are not same")
    else:
        print(calculate_transition_transversion_ratio(s_1,s_2)) 
