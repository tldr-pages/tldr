# bwa

> BWA is a short, low-divergent DNA sequences mapper against a large reference genome, such as the human genome.
> More information: <https://github.com/lh3/bwa>.

- Index reference genome:

`bwa index {{path/to/reference.fa}}`

- Map single-end reads (sequences) to indexed genome using 32 [t]*hreads and compress the result to save space:

`bwa mem -t 32 {{path/to/reference.fa}} {{path/to/read_single_end.fq.gz}} | gzip -3 > {{path/to/alignment_single_end.sam.gz}}`

- Map pair-end reads (sequences) to indexed genome using 32 [t]hreads and compress the result to save space:

`bwa mem -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip -3 > {{path/to/alignment_pair_end.sam.gz}}`

- Map pair-end reads (sequences) to indexed genome using 32 [t]hreads with [m]arking shorter split hits as secondary for output SAM file compatibility in Picard software and compress the result:

`bwa mem -M -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip -3 > {{path/to/alignment_pair_end.sam.gz}}`

- Map pair-end reads (sequences) to indexed genome using 32 [t]hreads with FASTA/Q [c]omments (e.g. BC:Z:CGTAC) appending to a compressed result:

`bwa mem -C -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip -3 > {{path/to/alignment_pair_end.sam.gz}}`

- Map single-end reads (sequences) shorter than ~70 bp to indexed genome using 32 [t]hreads and compress the result:

`bwa aln -t 32 {{path/to/reference.fa}} {{path/to/read_single_end.fq.gz}} > {{path/to/read_single_end.sai}}; bwa samse {{path/to/reference.fa}} {{path/to/read_single_end.sai}} {{path/to/read_single_end.fq.gz}} | gzip -3 > {{path/to/alignment_single_end.sam.gz}}`

- Map pair-end reads (sequences) shorter than ~70 bp to indexed genome using 32 [t]hreads and compress the result:

`bwa aln -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} > {{path/to/read_pair_end_1.sai}}; bwa aln -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_2.fq.gz}} > {{path/to/read_pair_end_2.sai}}; bwa sampe {{path/to/reference.fa}} {{path/to/read_pair_end_1.sai}} {{path/to/read_pair_end_2.sai}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip -3 > {{path/to/alignment_pair_end.sam.gz}}`
