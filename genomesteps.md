# What we need to do to analyze a genome after the sequencing?
# In this case, the genome was mounted and we need only do the follow steps

# CHECK THE MOUNT QUALITY, for this we used BUSCO
## We analyzed firstly the protein content against three different types of database
  #LAURASIATHERIA
python ../../../../dados/software/busco-master/scripts/run_BUSCO.py -i ../../../../dados/trichechus/results_tinunguis/Tinunguis.proteins.fasta -o Tinunguis -l ../../../../dados/trichechus/laurasiatheria_odb9/ -m prot -c 5
  #TETRAPODA
python ../../../../dados/software/busco-master/scripts/run_BUSCO.py -i ../../../../dados/trichechus/results_tinunguis/Tinunguis.proteins.fasta -o tetrapoda -l ../../../../dados/trichechus/tetrapoda_odb9/ -m prot -c 10
  #MAMMALIA
python ../../../../dados/software/busco-master/scripts/run_BUSCO.py -i ../../../../dados/trichechus/results_tinunguis/Tinunguis.proteins.fasta -o tetrapoda -l ../../../../dados/trichechus/tetrapoda_odb9/ -m prot -c 10
## We check the scaffold content against the same data base

# FILTER THE REPEAT ELEMENTS and identify LINEs, SINES and other elements using REPEATMASKER, this step is important to filter the big data due the fact that the next step is the prediction, and if you don't remove this the prediction could be imprecise
## Construct the database
/dados/software/RepeatModeler-open-1.0.11/BuildDatabase -name tinunguis.db -engine ncbi ../results_tinunguis/Tinunguis.scaffolds.fasta
## We need to run the REPEATMODELER, due the fact that we don't have the transcriptome (improve this explanation)
/dados/software/RepeatModeler-open-1.0.11/RepeatModeler -database tinunguis.db -engine ncbi -pa 30
## Run the REPEATMASKER
/dados/software/RepeatMasker/RepeatMasker -pa 30 -gff -lib RM_118180.TueMay210948422019/consensi.fa.classified ../../results_tinunguis/Tinunguis.scaffolds.fasta 
## RE-RUN the REPEATMASKER adding the command -xsmall that shows the repeat regions in small case
nohup /dados/software/RepeatMasker/RepeatMasker -pa 30 -xsmall -gff -lib RM_118180.TueMay210948422019/consensi.fa.classified ../../results_tinunguis/Tinunguis.scaffolds.fasta &

#GENE PREDICTION,to do this step we will use the software AUGUSTUS. The idea is use a training set from BUSCO, when we did the first step with BUSCO the software training using the scaffolds so we will test the prediction with this file and not HUMAN
## We need to prepare the training data set and put it on the AUGUSTUS file_SPECIES
## In this file, we have the training file generate by BUSCO
  /dados/trichechus/analises_erica/tinunguis_busco_genome/run_laurasiatheria/augustus_output/retraining_parameters  
## At first, we need to create a new file 
  /dados/trichechus/analises_erica/tinunguis_busco_genome/run_laurasiatheria/augustus_output/trichechus_inunguis
## Copy the retraining file to the new file 'trichechus_inunguis', the '*' copy all the contents of the file inside the other
  cp /dados/trichechus/analises_erica/tinunguis_busco_genome/run_laurasiatheria/augustus_output/retraining_parameters/* /dados/trichechus/analises_erica/tinunguis_busco_genome/run_laurasiatheria/augustus_output/trichechus_inunguis/
## Inside of the file 'trichechus_inunguis' we will change the file names
  mv BUSCO_laurasiatheria_2431351931_exon_probs.pbl trichechus_inunguis_exon_probs.pbl
  mv BUSCO_laurasiatheria_2431351931_igenic_probs.pbl trichechus_inunguis_igenic_probs.pbl
  mv BUSCO_laurasiatheria_2431351931_intron_probs.pbl trichechus_inunguis_intron_probs.pbl
  mv BUSCO_laurasiatheria_2431351931_metapars.cfg trichechus_inunguis_metapars.cfg
  mv BUSCO_laurasiatheria_2431351931_metapars.cgp.cfg trichechus_inunguis_metapars.cgp.cfg
  mv BUSCO_laurasiatheria_2431351931_metapars.utr.cfg trichechus_inunguis_metapars.utr.cfg
  mv BUSCO_laurasiatheria_2431351931_parameters.cfg trichechus_inunguis_parameters.cfg
  mv BUSCO_laurasiatheria_2431351931_weightmatrix.txt trichechus_inunguis_weightmatrix.txt
## Now we need to change the name inside the file 'trichechus_inunguis_parameters.cfg', to avoid error in AUGUSTUS
  sed -i 's/BUSCO_laurasiatheria_2431351931/trichechus_inunguis/g' trichechus_inunguis_parameters.cfg
           ###########This command is new for me###########################
           sed '/s/The_name_that_U_looking_for/The_new_name/g' namefile.txt
## We copy all the directory 'trichechus_inunguis' to AUGUSTUS file
cp -r /dados/trichechus/analises_erica/tinunguis_busco_genome/run_laurasiatheria/augustus_output/trichechus_inunguis/ /dados/public/miniconda3/config/species/
## With this steps in the parameter --species=SPECIES from AUGUSTUS, we will find --species=trichechus_inunguis
## We verify that AUGUSTUS in default usually use only 1 CPU, so to improve the analysis we decide to split the scaffolds and run each one:
## split.py
import os
print("Comecou")
arquivo = open("/dados/trichechus/analises_erica/Repeat_test/Tinunguis.scaffolds.fasta.masked.fasta", "r")

dic = {}

count_bp = 0
for line in arquivo:
        line = line.rstrip()
        if line.startswith(">"):
                name = line[1:]
                dic[name] = ""
        else:
                dic[name] = dic[name] + str(line)
arquivo.close()

count_files = 1
count_bp = 0

print(str(count_files) + " de 30")
os.mkdir("/dados/trichechus/analises_erica/augustus_lucas/divididos/1/")
new_arquivo = open("/dados/trichechus/analises_erica/augustus_lucas/divididos/1/Tinunguis.scaffolds.masked.1.fasta", "w")
for key, value in dic.items():
        count_bp = count_bp + len(value)
        if count_bp <= 105140235:
                new_arquivo.write(">" + str(key) + "\n" + str(value) + "\n")
        else:
                count_files += 1
                count_bp = 0
                new_arquivo.close()
                os.mkdir("/dados/trichechus/analises_erica/augustus_lucas/divididos/" + str(count_files) + "/")
                new_arquivo = open("/dados/trichechus/analises_erica/augustus_lucas/divididos/" + str(count_files) + "/Tinunguis.scaffolds.masked." + str(count_files) + ".fasta", "w")
                new_arquivo.write(">" + str(key) + "\n" + str(value) + "\n")
                print(str(count_files) + " de 30")

new_arquivo.close()
print("Acabou.")

## This commnad is used with python to split the scaffolds 

