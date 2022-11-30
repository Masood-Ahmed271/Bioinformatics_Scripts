'''
Description: Assignment 3 Question 9 -> Write a program which takes a set of reads as input (from inputQ9.txt)
                                       and constructs the de Bruijn graph for the reads.
Author: Masood Ahmed
UID: 3035812127

'''

'''
Description: Finding distinct kmers
parameters: lines --> a list of lines in the file
            k -> the size
return: a list of distinct kmers

'''
def find_kmers(lines, k=3):
    kSet = set()
    for i in lines:
        end = len(i.strip())-k+1
        for j in range(0, end):
            kSet.add(i[j:j+k])
    return sorted(list(kSet))

'''
Description: building a de_brujin graph
Parameters: kmers -> a list of distinct kmers
            lines --> a list of lines in the file
            k -> the size
return: a list of edges of de burjin graph

'''
def construct_de_bruijn_graph(kmers,lines, k=3):

    edges = []

    for i in kmers:
        for j in kmers:
            if i[1:k] == j[0:k-1] and  i != j:
                s = i[0:k] + j[k-1]
                if any(s in k for k in lines):
                    edges.append((i, j))
    return edges

'''
Description: Prints the answers as required
Parameters: kmers -> a list of distinct kmers
            lines --> a list of lines in the file

'''
def print_answer_final(kmers,edges):
    print('K-mers:')
    for each in kmers:
        print(each)
    
    print("Adjacency List:")
    for tup in edges:
        print(tup[0] + " " + tup[1])

# main program
if __name__ == "__main__":
    # Assuming that input is in the following form:
    # TACAGT
    # AGTCAG
    # ACAGTC
    # TCAGAT
    input_file = open('inputQ9.txt', 'r')
    lines = input_file.readlines() 
    kmers = find_kmers(lines, k=3)
    edges = construct_de_bruijn_graph(kmers,lines)
    print_answer_final(kmers,edges)
    input_file.close()


    
