##Looking for repeat elements using RepeatMasker
#Construct the database
/dados/software/RepeatModeler-open-1.0.11/BuildDatabase -name NOME.db -engine ncbi ../caminho_scaffolds/nome.scaffolds/fasta

#We need to run RepeatModeler due the fact that we don't have trasncriptome data to use in the next steps
/dados/software/RepeatModeler-open-1.0.11/RepeatModeler -database NOME.db -engine ncbi -pa 30

#After this step we need to have a file NAME.fa.classified to run RepeatMasker showing the repeat regions
nohup /dados/software/RepeatMasker/RepeatMasker -pa 30 -xsmall -gff -lib RM_caminhopasta/consensis.fa.classified ../caminhoscaffold/scaffold.fasta&

#At the end we have a table with the summary data and the masked scaffold
