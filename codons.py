def create_codon_dict(file_path):
     with open(file_path,'r') as codons_file:
          rows=codons_file.readlines()
          split_acids={}
          for row in rows:
              row=row.strip().split('\t')
              codon=row[0]
              amino=row[2]
              split_acids[codon]=amino 
     return split_acids
        

     

    


