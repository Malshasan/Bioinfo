# Bioinfo
python based bioinformatics programmes 
majority vating to predict protein function

1) Implementing the majority voting network-based candidate protein prediction algorithm. I.II. Write the steps of an algorithm to predict the majority voting score of unknown
proteins for a given function in a network. Assume that a list of known proteins
annotated to the particular function is given as a text file. This should output/print the
list of unknown proteins with the predicted majority voting score. """

Alogorithm

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
 obtain the know protein in the dreb's protein interaction
    dreb_knownp_union =(Dreb_ppi.intersection(set_known_protein))
 the difference of the dreb ppi - known protein in the breb protein network = unknown protein in the dreb protein network
dreb_unknown_protein =Dreb_ppi.difference(dreb_knownp_union)

