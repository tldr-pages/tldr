# samtools

> Tools for handling high-throughput sequencing (genomics) data.
> Used for reading/writing/editing/indexing/viewing of data in SAM/BAM/CRAM format.

- Convert a SAM input file (-S) to BAM stream (-b) and save to file:

`samtools view -bS {{input.sam}} > {{output.bam}}`

- Take input from stdin (-) and output a region, including the file header (-h). Prints to stdout:

`{{other_command}} | samtools view -h - chromosome:start-end`

- Sort a file and save using -o (format chosen by output file extension):

`samtools sort {{input}} -o {{output.bam}}`

- Index a sorted BAM file (creates {{sorted_input.bai}}):

`samtools index {{sorted_input}}`

- Print alignment statistics about a file:

`samtools flagstat {{sorted_input}}`

- Count alignments to each index (chromosome / contig):

`samtools idxstats {{sorted_indexed_input}}`

- Merge multiple files:

`samtools merge {{output}} {{input_1}} [{{input_2}}..{{input_n}}]`

- Split input file according to read groups:

`samtools split {{merged_input}}`
