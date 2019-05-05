#How to create an environment in miniconda3 at my lab server
# -y = proceed [y/n] and -n = environment name
conda create -y -n funannotate

#To create an environment with a specific version of Python and multiple packages
conda create -n myenv python=3.4 scipy=0.15.0 astroid babel. #example

#In our case the best command line were find in funannotate page. In this case the software is install with an specific python and other packages
conda create -y -n funannotate python=2.7 numpy pandas scipy matplotlib seaborn \
    natsort scikit-learn psutil biopython requests blast rmblast goatools fisher \
    bedtools blat hmmer exonerate diamond>=0.9 tbl2asn hisat2 ucsc-pslcdnafilter \
    samtools raxml trimal mafft>=7 iqtree kallisto bowtie2 infernal mummer minimap2 \
    trinity>=2.6.6 evidencemodeler pasa>=2.3 codingquarry stringtie gmap=2017.11.15 \
    ete3 salmon>=0.9 jellyfish>=2.2 htslib trnascan-se repeatmasker repeatmodeler \
    trf  perl-threaded perl-db-file perl-bioperl perl-dbd-mysql perl-dbd-sqlite \
    perl-text-soundex perl-scalar-util-numeric perl-data-dumper perl-dbi perl-clone \
    perl-json perl-logger-simple perl-hash-merge perl-yaml perl-pod-usage perl-getopt-long \
    perl-parallel-forkmanager perl-carp perl-app-cpanminus
    
# Here I find the others step, but still confuse to me: https://funannotate.readthedocs.io/en/latest/prepare.html

# So, let's try to begin the cleaning assembly, write:
funnanotate clean #you'll see a couple of commands

# Remenber to export the packages:
export BAMTOOLS_PATH=/dados/trichechus/analises_erica/bamtools
export FUNANNOTATE_DB=/dados/trichechus/analises_erica/DB/
export GENEMARK_PATH=/dados/public/gm_et_linux_64/gmes_petap
export AUGUSTUS_CONFIG_PATH=/dados/public/miniconda3/config/
export PASAHOME=/dados/public/miniconda3/envs/funannotate/opt/pasa-2.3.3/
export TRINITYHOME=/dados/public/miniconda3/envs/funannotate/opt/trinity-2.6.6/
export EVM_HOME=/dados/public/miniconda3/envs/funannotate/opt/evidencemodeler-1.1.1/

# Repeating masking the scaffolds
nohup funannotate mask -i /dados/trichechus/results_tinunguis/Tinunguis.scaffolds.fasta -o tinumask --cpus 15 &
