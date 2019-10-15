#We need to prepare the file after the annotation. For this we will create a file with cds of Trichechus
#We will create a list with the headers of /dados/trichechus/final_prediction/inunguis/T_inunguis.blast_uniprot.fasta
#After this we will do an dictionary using /dados/trichechus/final_prediction/inunguis/augustus.hints.codingseq we will looping and create a file with sequences based on the list created
#Follow the commands

# Criar a lista com os headers ok
anotation = [] 

head = open("T_inunguis.blast_uniprot.fasta", "r")
for line in head:
	line = line.rstrip()
	if line.startswith(">"):
		anotation.append(line[1:])
	else:
		pass
head.close()


# Criar o dic com a predição do augustus
notation = {}

arquivo = open("augustus.hints.codingseq", "r")

for line in arquivo:
        line = line.rstrip()
        if line.startswith(">"):
                id_gene = line[1:]
                notation[id_gene] = ""
        else:
                notation[id_gene] = notation[id_gene] + line
arquivo.close()

# Criar um arquivo com o CDS baseado no blast do uniprot
new_file = open("/dados/trichechus/final_prediction/inunguis/T_inunguis.fasta", "w")
for key, value in notation.items():
        if key in anotation:
                new_file.write(">TINUN" + str(key) + "\n" + str(value) + "\n")
        else:
                pass
new_file.close()
