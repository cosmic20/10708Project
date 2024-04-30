# 10708Project

## Background

Despite its significantly lower mutation rate compared to Influenza A, COVID-19 has continued to evolve since its emergence in late 2019, necessitating the annual reformulation of vaccines as recommended by the FDA each autumn. As humanity contends with the ongoing cycle of virus evolution and the corresponding development of treatments and vaccines, understanding the genomic intricacies of COVID-19 remains essential. Historically, scientists have adapted influenza vaccines based on phylogenetic and statistical analyses of global surveillance data, which track the evolution and spread of virus strains.

With recent advancements, artificial intelligence now enhances these predictions by processing complex data more efficiently than traditional methods, potentially uncovering patterns that were previously undetectable. In our study, we applied graphical methods discussed in our course to see if these tools can produce plausible mutated sequences of COVID-19. We specifically assessed Hidden Markov Models, Variational Autoencoders, and Generative Adversarial Networks, to evaluate their effectiveness.

To measure the success of the methods, which we compared the GC content of our generated sequences and performed local alignment against a consensus COVID-19 genome. This dual approach not only tests the structural accuracy of our models but also their practical applicability in simulating the evolutionary dynamics of the virus.


## Methods 

To run HMM, run hmm.py. 

To run GAN by itself, run the GAN_SequenceGeneration.ipynb file. It contains the full GAN architecture and the training and sequences generated. 

To run VAE by itself,run the torch_geom.ipynb file. It generates the de Bruijn graphs for all the sequences, and feeds into the VAE. You can specify the k-mer size that you want when creating the k-mer dictionary.

To run VAE+GAN.
1) genereate the fragmented sequences in the cell with the comment #FRAGMENTED SEQUENCES NOT FULL
2) the second to last cell trains and generates sequences of the VAE_GAN model

For assessment of the sequences generated, run Alignment_Testing_Algorithms.ipynb. It contains reading input files in Generated_Sequences/ and computes the GC Content of the COVID-19 Reference Genome and the average for each of the generated sequences. The file also contains the Smith-Waterman Algorithm for Local Alignment between each of the sequences to the reference genome. 
