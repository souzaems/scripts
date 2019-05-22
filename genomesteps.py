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
##Construct the database
/dados/software/RepeatModeler-open-1.0.11/BuildDatabase -name tinunguis.db -engine ncbi ../results_tinunguis/Tinunguis.scaffolds.fasta
##We need to run the REPEATMODELER, due the fact that we don't have the transcriptome (improve this explanation)
/dados/software/RepeatModeler-open-1.0.11/RepeatModeler -database tinunguis.db -engine ncbi -pa 30
##Run the REPEATMASKER
/dados/software/RepeatMasker/RepeatMasker -pa 30 -gff -lib RM_118180.TueMay210948422019/consensi.fa.classified ../../results_tinunguis/Tinunguis.scaffolds.fasta 

