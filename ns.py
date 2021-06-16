from Bio import Entrez
Entrez.email = "amit34655@gmail.com"
rec = Entrez.read(Entrez.esearch(db="protein", term="Homo Sapiens AND Tumor Protein 53" ))
print(rec['IdList'])
p_handle = Entrez.efetch(
  db="protein", id=rec["IdList"], rettype="fasta", retmode="text"
)
print(p_handle.read())
