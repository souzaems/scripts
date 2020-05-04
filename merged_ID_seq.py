# You must do a dictionay using you database
arquivo = open("file.fa","r")
dic_fasta = {}
for line in arquivo:
	line = line.rstrip()
	if line.startswith(">"):
		key_name = line[1:]
		dic_fasta[key_name] = ""
	else:
		dic_fasta[key_name] = dic_fasta[key_name] + str(line)
print("dic created")
# Now you must do a list with the ID's that you looking for
lista_tmana = open("onlyID.txt","r")
lista_ID = []
for line in lista_tmana:
	line = line.rstrip()
	if line.startswith(">"):
		name = line[1:]
		lista_ID.append(name)
	else:
		pass
	arquivo.close()
# Now you must to get a looping in those files
onlymana = open("results.fa","w")
for key, value in dic_fasta.items():
	if key in lista_ID:
		onlymana.write(">" + str(key) + "\n" + str(value) + "\n")
onlymana.close()
print("done")
