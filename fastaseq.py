from Bio import Entrez
Entrez.email = "example@oregonstate.edu"
p_handle = Entrez.efetch(db="protein", id='4507341', rettype="gb", retmode="text")
print(p_handle.read())