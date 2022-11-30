'''
Assignment 2 (Section 2 - Q7)
Author: Masood AHMED
UID: 3035812127
Email_Address: masood20@connect.hku.hk
Description: In a weighted alphabet, every symbol is assigned a positive real number called a weight. A
string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum
of the weights of its symbols. The standard weight assigned to each member of the 20-symbol amino acid
alphabet is the monoisotopic mass of the corresponding amino acid. This program will find the total weight of PP.

'''

'''
Desription: This is a function that takes protein string pp and calculates the total weight of the PP.
Parameters: ProteinString --> protein string pp
Return:     ret --> total wight of the pp

'''
def calculatingMassProtein(ProteinString):

    ret = 0        # a variable that stores the wight of the PP

    #monoisotopic mass table
    protein_mass= { 'A': 71.03711, 'R': 156.10111, 'N': 114.04293,
	              'D': 115.02694, 'C': 103.00919, 'E': 129.04259,
	              'Q': 128.05858, 'G': 57.02146, 'H': 137.05891,
	              'I': 113.08406, 'L': 113.08406, 'K': 128.09496,
	              'M': 131.04049, 'F': 147.06841, 'P': 97.05276,
	              'S': 87.03203,  'T': 101.04768, 'W': 186.07931,
	              'Y': 163.06333, 'V': 99.06841
                }

    # a lopp to calculate the weight
    for protein in ProteinString:
        if protein in protein_mass:
            ret+=protein_mass[protein]
    # rouding off to 5 decimal places.
    return round(ret, 5)

'''
From where the program starts

'''
if __name__ == "__main__":

    ProteinString = input("Please input a protein string PP of length at most 1000 amino acid: ")
    print(calculatingMassProtein(ProteinString))