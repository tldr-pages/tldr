# samtools

> Tools for handling high-throughput sequencing (genomics) data.
> Reading/writing/editing/indexing/viewing of data in SAM/BAM/CRAM format.

- Convert a SAM file to BAM (use - for stdin):

`samtools view -bS {{input.sam}} > {{output.bam}}`

- Print a region of a file, include the file header:

`samtools view -h {{input}} chr:start-end > {{output.sam}}`

- Sort a file:

`samtools sort -m {{memory_per_cpu}} -@ {{cpus}} {{input}} -o {{output.bam}}`

- Index a sorted BAM file:

`samtools index {{sorted_input}}`

- Print alignment statistics about a file:

`samtools flagstat {{sorted_input}}`

- Count alignments to each index (chromosome / contig):

`samtools idxstats {{sorted_indexed_input}}`
