# bwa

> Burrows-Wheeler比对工具。
> 针对大型参考基因组（例如人类基因组）进行短的、低差异的DNA序列映射。
> 更多信息：<https://github.com/lh3/bwa>。

- 索引参考基因组：

`bwa index {{path/to/reference.fa}}`

- 使用32个线程将单端读取（序列）映射到索引基因组，并压缩结果以节省空间：

`bwa mem -t 32 {{path/to/reference.fa}} {{path/to/read_single_end.fq.gz}} | gzip > {{path/to/alignment_single_end.sam.gz}}`

- 使用32个线程将双端读取（序列）映射到索引基因组，并压缩结果以节省空间：

`bwa mem -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip > {{path/to/alignment_pair_end.sam.gz}}`

- 使用32个线程将双端读取（序列）映射到索引基因组，并将短的拆分比对标记为输出SAM文件兼容的次要比对，以便于Picard软件使用，并压缩结果：

`bwa mem -M -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip > {{path/to/alignment_pair_end.sam.gz}}`

- 使用32个线程将双端读取（序列）映射到索引基因组，并附加FASTA/Q注释（例如BC:Z:CGTAC）到压缩结果：

`bwa mem -C -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip > {{path/to/alignment_pair_end.sam.gz}}`