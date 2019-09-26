# After the analysis of blast results, you should pick the best fragments from the big scaffold file
arquivo = open("NAME.scaffolds.masked.fasta", "r") #read the file
dic_fasta = {} #we'll create a dictionary
for line in arquivo:
		line = line.rstrip()
        if line.startswith(">"):  #the program will looking for this symbol
                key_name = line[1:]
                dic_fasta[key_name] = ""
        else:
                dic_fasta[key_name] = dic_fasta[key_name] + str(line)
for key, value in dic_fasta.items():
        if key == "flattened_line_18126_pilon": #this's the name of one of select scaffolds
        	print(">SeqA" + "\n" + value[16348:22348] + "\n")  #the fragments position
        	print(">SeqB" + "\n" + value[6678:12024] + "\n")
        	print(">SeqC" + "\n" + value[1637:12035] + "\n")
        elif key == "scaffold_4115_uid_1549280921": #if you have more than one scaffold use ELIF
        	print(">SeqD" + "\n" + value[47811:60016] + "\n")
        	print(">SeqE" + "\n" + value[44867:47800] + "\n")
		elif key =="scaffold_7342_uid_1549280921":
			print(">SeqF" + "\n" + value[12063:14965] + "\n") #you can change the name of each fragment
			print(">SeqG" + "\n" + value[9492:11756] + "\n")
		else:
			pass
      
 # To run this file I suggest to use the command python extract_frag_scaffolds.py > name.fasta , this will return a fasta file with all the fragments selected
