def create_codon_dict(file_path):
    split_acids={}
     with open(flie_path,'r') as codons_file:
           for row in codons_file.readlines():
               row=row.strip().split('/t')
               split_acids={row[0]:row[2]}
        codons_file.close()
         return split_acids
        

     

    


