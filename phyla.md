**Mr Bayes**

BEGIN MRBAYES;

outgroup M_sp_1_MA_13;

lset nst=6 rates=equal;

mcmcp ngen= 15000000 relburnin=yes burninfrac=0.25 printfreq=1000  samplefreq=1000 nchains=4 savebrlens=yes;

mcmc;

sump;

sumt;

sump;

end;

**RaxML**

*Bootstraping*

raxmlHPC -m GTRGAMMA -p 12345 -b 12345 -# 100 -s dna.phy -n T14 

*Rapid bootstraping*

raxmlHPC -m GTRGAMMA -p 12345 -x 12345 -# 100 -s dna.phy -n T19 

**Partitioned analysis*

raxmlHPC -m GTRGAMMA -p 12345 -q simpleDNApartition.txt -s dna.phy -n T21 
