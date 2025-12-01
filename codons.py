def create_codon_dict(file_path):
    split_acids={}
     with open(file_path,'r') as codons_file:
           for row in codons_file.readlines():
               rows=row.strip().split('\t')
               split_acids[rows[0]]=rows[2]
    return split_acids
        

     

    


