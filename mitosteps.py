# The current address to go to MITObim
https://github.com/chrishah/MITObim/blob/master/README.md

# After the creation of directory tutorial1
# montagem do genoma mitocondrial com genoma de referencia
mkdir tutorial1
cd tutorial1

#Caminho do MIRA 4
/dados/erica/mtDNA/mira_4.0.2/bin/mira

# Link the files
ln -s /dados/erica/mtDNA/MITObim-master/testdata1/Tthymallus-150bp-300sd50-interleaved.fastq reads.fastq 
ln -s /dados/erica/mtDNA/MITObim-master/testdata1/Salpinus-mt-genome-NC_000861.fasta reference.fa

# Using manifest file
echo -e "\n#manifest file for basic mapping assembly with illumina data using MIRA 4\n\nproject = initial-mapping-testpool-to-Salpinus-mt\n\njob=genome,mapping,accurate\n\nparameters = -NW:mrnl=0 -AS:nop=1 SOLEXA_SETTINGS -CO:msr=no\n\nreadgroup\nis_reference\ndata = reference.fa\nstrain = Salpinus-mt-genome\n\nreadgroup = reads\ndata = reads.fastq\ntechnology = solexa\nstrain = testpool\n" > manifest.conf

# To see the manifest.conf
head -n 20 manifest.conf

# Run MIRA 4
/dados/erica/mtDNA/mira_4.0.2/bin/mira manifest.conf

# Run MITO 1.9 in the main file that have the file read.sew
/dados/erica/mtDNA/MITObim-master/MITObim.pl -start 1 -end 10 -sample testpool -ref Salpinus_mt_genome -readpool reads.fastq -maf initial-mapping-testpool-to-Salpinus-mt_assembly/initial-mapping-testpool-to-Salpinus-mt_d_results/initial-mapping-testpool-to-Salpinus-mt_out.maf &> log
