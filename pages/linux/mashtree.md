# Mashtree

> Makes a fast tree from genomes.
> Does not make a phylogeny.
> Home page is [https://github.com/lskatz/mashtree](https://github.com/lskatz/mashtree).

- Fastest method:

`mashtree --numcpus 12 *.fastq.gz [*.fasta] > mashtree.dnd`

- Most accurate method:

`mashtree --mindepth 0 --numcpus 12 *.fastq.gz [*.fasta] > mashtree.dnd`

- Add confidence values (note the `--` to separate options specific to bootstrapping):

`mashtree_bootstrap.pl --reps 100 --numcpus 12 *.fastq.gz -- --min-depth 0 > mashtree.bootstrap.dnd`
