# mashtree

> Make a fast tree from genomes.
> Does not make a phylogeny.
> More information: <https://github.com/lskatz/mashtree>.

- Fastest method in mashtree to create a tree from fastq and/or fasta files using multiple threads, piping into a newick file:

`mashtree --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} > {{mashtree.dnd}}`

- Most accurate method in mashtree to create a tree from fastq and/or fasta files using multiple threads, piping into a newick file:

`mashtree --mindepth {{0}} --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} > {{mashtree.dnd}}`

- Most accurate method to create a tree with confidence values (note that any options for `mashtree` itself has to be on the right side of the `--`):

`mashtree_bootstrap.pl --reps {{100}} --numcpus {{12}} {{*.fastq.gz}} -- --min-depth {{0}} > {{mashtree.bootstrap.dnd}}`
