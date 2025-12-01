def create_codon_dict(file_path):
    split_acids={}
     with open(flie_path) as codons_file:
           for row in codon_file.readlines():
               row.strip()
               row.split('/t')
               split_acids={row[0]:row[2]}
        codon_file.close()
         return split_acids
        

     

    


