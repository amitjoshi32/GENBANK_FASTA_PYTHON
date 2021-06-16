from Bio import Entrez
Entrez.email = "amit34655@gmail.com"
rec = Entrez.read(Entrez.esearch(db="protein", term="NP_003173"))
print(rec['IdList'])
p_handle = Entrez.efetch(
  db="protein", id=rec["IdList"][0], rettype="fasta", retmode="text"
)
print(p_handle.read())