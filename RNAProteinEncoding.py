'''
Author: Masood Ahmed
UID: 3035812127
Email: masood20@connect.hku.hk

Description: This program takes a RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
             and returns the protein string encoded by s.

Assumption: Every Base and Protein Encoding is UpperCase

'''

# creating a dictionary to store all the possible protein encodings which we will use for mapping to RNA string sequences
proteinCodings = {
'UUC':'F','CUC':'L','AUC':'I','GUC':'V','UUA':'L','CUA':'L','AUA':'I','GUA':'V',
'UCU':'S','CCU':'P','ACU':'T','GCU':'A','UCC':'S','CCC':'P','ACC':'T','GCC':'A',
'UAU':'Y','CAU':'H','AAU':'N','GAU':'D','UCA':'S','CCA':'P','ACA':'T','GCA':'A',
'UUG':'L','CUG':'L','AUG':'M','GUG':'V','UCG':'S','CCG':'P','ACG':'T','GCG':'A',
'UUU':'F','CUU':'L','AUU':'I','GUU':'V','UAC':'Y','CAC':'H','AAC':'N','GAC':'D',
'UAA':'stop','CAA':'Q','AAA':'K','GAA':'E','UGA':'stop','CGA':'R','AGA':'R','GGA':'G',
'UGU':'C','CGU':'R','AGU':'S','GGU':'G','UGC':'C','CGC':'R','AGC':'S','GGC':'G',
'UAG':'stop','CAG':'Q','AAG':'K','GAG':'E','UGG':'W','CGG':'R','AGG':'R','GGG':'G'
}

'''

A function that translates RNA to protein coding
Parameter: String --> An RNA sequence
Return: String --> The Encoding

'''
def translatingRNA(seq):
    proteinEncoding = ''     # the string where we will store the protien encoding
    ind = seq.find("AUG")     # finding the starting point
    # if starting point is not found, we cannot start transaltion
    if ind == -1:
        return "transaltion can't be done."
    while ind < len(seq):
        triplet = seq[ind:ind+3]
        if proteinCodings[triplet] == 'stop':
            return proteinEncoding
        ind += 3
        proteinEncoding += proteinCodings[triplet]
    return proteinEncoding

if __name__ == '__main__':
    seq = 'GAUGGGGAGUACCCGUUAAAACGGGAUGGCCAUGGCGCCCAGAACUGAG'
    encoding = translatingRNA(seq)
    print(encoding)
