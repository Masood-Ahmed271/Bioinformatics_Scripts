'''
    Author: Masood Ahmed
    Email: masood20@connect.hku.hk
    UID: 3035812127
    Description: This program will count the GC content in the substring and will keep track
                 of the substrings of length 100 that have a GC content of 70%.
'''

# Opening an input file.
inputFile = open("chr22.fa", "r")

# Reading the line 1 and line 2
sequenceName = inputFile.readline()
seq = inputFile.readline()

# Starting 100 base pairs
ind = 0 
k = 100
# to keep track of high GC content substrings
GCSubstings = 0
# looping through the entire genome sequence and counting c's and g's and if they are
# greater than 70 in 100 base pairs, then incrementing GCSubstring variable.
while ind < len(seq) - k + 1:
    # For debugging purpose because program runs for a long time
    print("Running    >> " + str(len(seq)) + " >> current index >> " + str(ind))
    subString = seq[ind:ind+k]
    gcCount = 0
    for ch in subString:
        ch = ch.lower()
        if ch == 'g' or ch == 'c':
            gcCount+=1
    if gcCount > 70:
        GCSubstings+=1
    ind += 1

# For debugging purpose because program runs for a long time
print("-------------------------")
print("-------------------------")
print("-------------------------")
print("-------------------------")
print("Done")
print("Answer")
# total number of GC high substrings
print(GCSubstings)
# closing the files
inputFile.close()
