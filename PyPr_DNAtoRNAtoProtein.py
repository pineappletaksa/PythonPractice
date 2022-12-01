#Convert DNA string into RNA by taking the filename and running either code_name.py --rna dna.txt or code_name.py --genes dna.txt 
#Takes DNA and converts it into RNA and into protein
#Procure DNA sequence

from sys import argv

def rna_operation(filename):
    dna = open(filename, "r")

#Convert DNA to RNA

    rna = dna.read().replace("T", "U")
    print "RNA:" + rna


#Convert RNA to protein
# " *** " are the stop codons

cdna_triplet = {
                   "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                   "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                   "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                   "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                   "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                   "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                   "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                   "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                   "TAT":"Y", "TAC":"Y", "TAA":" *** ", "TAG":" *** ",
                   "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                   "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                   "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                   "TGT":"C", "TGC":"C", "TGA":" *** ", "TGG":"W",
                   "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                   "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                   "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                   }


def genes_operation(filename, start, cdna_triplet):
    dna = open(filename, "r")
    dna_string = dna.read()
    start = dna_string.find("ATG")
    protein_seq = ""
    len(dna.read())
    for i in xrange (start, len(dna_string), 3):
       codon = dna_string[i:i+3]
       protein_seq += cdna_triplet[codon]
       
       print protein_seq
       print                                                                            
       print "Protein:"
       print " The (***) symbol represents a stop codon." 
       

filename, option, target = argv

if option == "--rna":
    rna_operation(target)
elif option == "--genes":
    print "This is the protein output of your file:" + target
    genes_operation(target, 0, cdna_triplet)
