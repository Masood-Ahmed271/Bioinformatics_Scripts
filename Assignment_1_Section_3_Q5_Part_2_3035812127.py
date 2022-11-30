'''
    Author: Masood Ahmed
    Email: masood20@connect.hku.hk
    UID: 3035812127
    Description: This program will mask the G and C's to n or N
'''

# Opening an input file and creating an output file.
inputFile = open("chr22.fa", "r")
outputFile = open("chr22.masked.fa", "w+")

# Reading the line 1 and line 2
sequenceName = inputFile.readline()
seq = inputFile.readline()

# putting the sequence name in the output file as required
outputFile.write(sequenceName)
outputFile.flush()

# to keep track of what bases have to be changed to n or N
tracker = [1]*len(seq)

# Starting 100 base pairs
ind = 0 
k = 100
# to keep track of high GC content substrings
GCSubstings = 0
# looping through the entire genome sequence and counting c's and g's and if they are
# greater than 70 in 100 base pairs, making the equivalent index in tracker to 0 
# indicating it should be masked.
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
        for tra in range(ind, ind+k):
            tracker[tra] = 0
    ind += 1

# Changing the substrings and masking them here according to the information
# of the tracker and writing them down in the output file.
for base in range(len(seq)):
    if tracker[base] == 0:
        if seq[base].islower():
            outputFile.write('n')
        else:
            outputFile.write('N')
    else:
        outputFile.write(seq[base])

# For debugging purpose
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
outputFile.close()
