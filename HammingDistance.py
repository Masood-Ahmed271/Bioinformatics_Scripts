'''
Assignment 2 (Section 2 - Q6)
Author: Masood AHMED
UID: 3035812127
Email_Address: masood20@connect.hku.hk
Description: Given two strings s and t of equal length, the Hamming distance between s and t, denoted
dH(s,t), is the number of corresponding symbols that differ in s and t.

'''


'''
Desription: This is the first approach to find the hamming distance. In this function, we take to DNA strings and 
            find the number of mismatches between them and return the number of mismatches. (Use this approach for marking)
Parameters: DNA_1 --> DNA string 1
            DNA_2 --> DNA string 2
Return:     ret --> number representing the mismatches

'''
def hamming_approach_1(DNA_1, DNA_2):
    ret = 0
    for i in range(len(DNA_1)):
        if DNA_1[i] != DNA_2[i]:
            ret+=1
    return ret

'''
Desription: This is the second approach to find the hamming distance which I just used to
            explore the zip function of python. In this function, we take to DNA strings and 
            find the number of mismatches between them and return the number of mismatches.
Parameters: DNA_1 --> DNA string 1
            DNA_2 --> DNA string 2
Return:     ret --> number representing the mismatches

'''
def hamming_approach_2(DNA_1,DNA_2):
    # The zip() function returns a zip object, which is an iterator of tuples where
    # the first item in each passed iterator is paired together, and then the second
    # item in each passed iterator are paired together etc.
    return len([(n1,n2) for n1, n2 in zip(DNA_1,DNA_2) if n1 != n2])


'''
From where the program starts

'''
if __name__ == "__main__":
    DNA_1 = input("Please input DNA sequence 1: ")
    DNA_2 = input("Please input DNA sequence 2: ")
    print()
    if len(DNA_1) != len(DNA_2):
        print("As sequence lengths are not same, hamming distance can't be calculated")
    else:
        print("Answer from Approach 1")
        print(hamming_approach_1(DNA_1, DNA_2))
        print("Answer from Approach 2")
        print(hamming_approach_2(DNA_1, DNA_2))

# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
