# mashtree

> Make a fast tree from genomes.
> Does not make a phylogeny.
> More information: <https://github.com/lskatz/mashtree#usage>.

- Create a tree from fastq and/or fasta files using the fastest method with multiple threads, piping into a newick file:

`mashtree --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} > {{mashtree.dnd}}`

- Create a tree from fastq and/or fasta files using the most accurate method with multiple threads, piping into a newick file:

`mashtree --mindepth {{0}} --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} > {{mashtree.dnd}}`

- Create a tree with confidence values using the most accurate method (note that any options for `mashtree` itself have to be on the right side of the `--`):

`mashtree_bootstrap.pl --reps {{100}} --numcpus {{12}} {{*.fastq.gz}} -- --min-depth {{0}} > {{mashtree.bootstrap.dnd}}`
