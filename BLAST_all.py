#In our server the blast package is on the genome environment
conda activate genome

#Construct the database(DB)
makeblastdb -in ondevcvaiprocurar.fasta -dbtype nucl # -dbtype nucl, prot

# PARA REALIZAR O BLAST EXISTEM DOIS FORMATOS DE SAÍDA, O TABULAR COM OS COMANDOS ABAIXO
#blastn -query seuarquivo.fasta -db ondevcvaiprocurar.fasta -out podemudaronome.outfmt6 -evalue 1e-20 -num_threads 2 -outfmt 6

#### -query é a sequencia q vc quer procurar, -out nome do output, -db nome do seu banco de dados, eg:
#### blastn -query tmanatusmt.fasta -db Tinunguis.scaffolds.fasta.masked.fasta -out blastn.outfmt6 -evalue 1e-20 -num_threads 2 -outfmt 6

#In this format we will have the output similar to NCBI
blastn -query whati'mlookingfor.fasta -db nameofDB.fasta -out frag.outfmt6 -evalue 1e-20 -num_threads 2 

## sempre que houver -num_threads é o numero de processadores q vc for usar, consulte seu coleguinha, se pouca gente tiver usando o servidor vc pode aumentar esse valor###
