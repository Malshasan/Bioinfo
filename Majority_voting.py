"""
Input - known function of protein/ PPI tsv file
Output - Unknow protein,majority voting

open tsv file
  rows = file.readlines
  for line in rows:
    skip the header
    split by |t
    node1 = split[0]
    nodee2 = split[2]
    weight = float(split[12])
    nx.write_gml

    text file --- known protein
     kwonw set{}
     open file
     readlines
     split"/t"
     for lines in rows:
        set.append{split[1]}


    #dreb2A interaction unknown protein for first level
    # obtain the know protein in the dreb's protein interaction
dreb_knownp_union =(Dreb_ppi.intersection(set_known_protein))

# the difference of the dreb ppi - known protein in the breb protein network = unknown protein in the dreb protein network
dreb_unknown_protein =Dreb_ppi.difference(dreb_knownp_union)


    #first level neighbor
    1_unknown_set = set_unknown union dreb_n{}

    initiate score dict

    #count majority
    for aa in 1_unknown_set:
        set_inter_unknown = {nlist(aa) intersection set_known()}
        majority_vote = len(set_inter_unknown)

        score_dict[] = majority_vote
    print(score dict)
 """
from fileinput import close
from itertools import count

import networkx as nx
pro_network = nx.Graph()#initate graph
from collections import OrderedDict

#creating graph object
with open("string_interactions.tsv", "r") as interaction_file:
    rows = interaction_file.readlines()#read tsv file by lines

    for line in rows:
        if "#" not in line and line.strip():#remove header
            linesplit = line.split('\t')
            node1 = linesplit[0]
            node2 = linesplit[1]
            pro_network.add_edge(node1, node2) #add edge


    print("Degree of the protien DREB1A is ",pro_network.degree["DREB2A"])

    #dreb interaction proteins

    Dreb_ppi =set(list(pro_network.neighbors("DREB2A")))
    print(Dreb_ppi)
interaction_file.close()

#set of known protein
with open("AT_stress_proteins.txt", "r") as interaction_file2:
    lines = interaction_file2.readlines()#read tsv file by lines
    set_known_protein = set()
    for line in lines:
        if "#" not in line and line.strip():#remove header
            linesplit = line.split('\t')
            known_proteinr = linesplit[1]
            set_known_protein.add(known_proteinr)

    #set_known_protein = set(known_protein)
    print(set_known_protein)
    print(len(set_known_protein))

interaction_file2.close()

#dreb2A interaction unknown protein for first level

dreb_knownp_union =(Dreb_ppi.intersection(set_known_protein)) # obtain the know protein in the dreb's protein interaction
print(len(dreb_knownp_union))
# the difference of the dreb ppi - known protein in the breb protein network = unknown protein in the dreb protein network
dreb_unknown_protein =Dreb_ppi.difference(dreb_knownp_union)

print(dreb_unknown_protein)
print("Unknown protein count of DREB2A",len(dreb_unknown_protein))

#conting majority voting for each know protein in the set
majority_dict = {}
for aa in dreb_unknown_protein:
    # get the protein interactions of the protein as a set
    aa_ppi = set(list(pro_network.neighbors(aa)))

    #majority vote
    #get the set -len of intersection of known protein and ppi set of protein
    vote = len(aa_ppi.intersection(set_known_protein))

    majority_dict[aa] =vote
    #print("protein is",aa,"vote is",vote)
print(majority_dict)

#print according to the desc vote
desc_score = OrderedDict(sorted(majority_dict.items(), key=lambda x:x[1], reverse=True))
print(desc_score)

#write in a file
with open("majority_score.txt","w") as file:
    for protein,score in desc_score.items():
        file.write(f"{protein}\t{score}\n")
file.close()




