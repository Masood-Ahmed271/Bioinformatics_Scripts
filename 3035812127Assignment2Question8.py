'''
Assignment 2 (Section 3 - Q8)
Author: Masood AHMED
UID: 3035812127
Email_Address: masood20@connect.hku.hk
Description: Implementing a Burrows-Wheeler-Transform (BWT) encoder

'''



'''
Desription: This is function returns the permutations of all the possible cyclic rotations
Parameters: seq --> sequence for which rotation permutations need to be found
Return:     rotation_matrix --> a list of all possible rotations in cyclic order

'''
def rotation(seq):

    rotation_matrix = []
    list_seq = list(seq)     # because string is not mutable in python

    # A loop where rotation takes place
    for i in range(len(seq)):
        temp = list_seq.pop(0) # getting the first index
        list_seq.append(temp)
        x = list_seq.copy()
        y = "".join(x)
        rotation_matrix.append(y)
    
    return rotation_matrix




'''
Desription: This is function is the implmentation of the BWT encoder
Parameters: seq --> sequence to be encoded
Return:     ret --> encoded sequence

'''
def BWT_encoder(seq):

    # appending the special character $
    seq+='$'
    ret = ""
    # doing a rotation
    possible_rotation = rotation(seq)
    # doing sorting
    sorted_list = sorted(possible_rotation)
    # getting the last letters
    for st in sorted_list:
        ret+=st[-1]
    # returning the encoded string
    return ret




'''
The place from where the program would start

'''
if __name__ == "__main__":
    seq = input()
    # Getting the encoded string
    print(BWT_encoder(seq))
