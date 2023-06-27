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
