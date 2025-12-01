def create_codon_dict(file_path):
    split_acids={}
     with open(file_path,'r') as codons_file:
           for row in codons_file.readlines():
               row=row.strip().split('\t')
                codon=row[0]
                amino=row[2]
               split_acids[codon]=amino 
    return split_acids
        

     

    


