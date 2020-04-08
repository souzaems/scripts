#First script > extract the big fragment from genome
arquivo = open("/dados/genomas/X_genoma_DB/Sfluviatilis.scaff
olds.fasta.masked.fasta", "r")
count = 0

for line in arquivo:
	line = line.rstrip()
	if count == 1 and ">" in line:
		break
	if "scaffold_612_uid_1558006649" in line:
		count = 1
	if count == 1:
		print(line)
    
#Call this script like this python get.py > frag.fasta
##################################################
#Second script
arquivo = open("/dados/X/zteste/osmo/scaffold_612_uid_1558006649.fa
sta", "r")

dic_fasta = {}
for line in arquivo:
	line = line.rstrip()
	if line.startswith(">"):
		key_name = line[1:]
		dic_fasta[key_name] = ""
	else:
		dic_fasta[key_name] = dic_fasta[key_name] + str(line)

for key, value in dic_fasta.items():
	print(">SeqA" + "\n" + value[312765:313030] + "\n")
	print(">SeqB" + "\n" + value[316753:316979] + "\n")
	print(">SeqC" + "\n" + value[326935:327161] + "\n")
	print(">SeqD" + "\n" + value[325131:325343] + "\n")
	print(">SeqE" + "\n" + value[320553:320746] + "\n")
	print(">SeqF" + "\n" + value[313195:313382] + "\n")
	print(">SeqG" + "\n" + value[327501:327676] + "\n")
	print(">SeqH" + "\n" + value[318818:318995] + "\n")
	print(">SeqI" + "\n" + value[323353:323512] + "\n")
  
#You can call python get2.py > final.fasta
