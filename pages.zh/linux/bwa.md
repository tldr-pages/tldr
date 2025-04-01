# bwa

> Burrows-Wheeler 对齐工具。
> 用于将短的、低分歧的 DNA 序列比对到大型参考基因组，如人类基因组。
> 更多信息：<https://manned.org/bwa>.

- 为参考基因组建立索引：

`bwa index {{path/to/reference.fa}}`

- 使用 32 个线程将单端读取（序列）比对到已索引的基因组，并压缩结果以节省空间：

`bwa mem -t 32 {{path/to/reference.fa}} {{path/to/read_single_end.fq.gz}} | gzip > {{path/to/alignment_single_end.sam.gz}}`

- 使用 32 个线程将双端读取（序列）比对到已索引的基因组，并压缩结果以节省空间：

`bwa mem -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip > {{path/to/alignment_pair_end.sam.gz}}`

- 使用 32 个线程将双端读取（序列）比对到已索引的基因组，并在输出的 SAM 文件中使用 Picard 软件兼容的方式标记较短的分裂比对，并压缩结果：

`bwa mem -M -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip > {{path/to/alignment_pair_end.sam.gz}}`

- 使用 32 个线程将双端读取（序列）比对到已索引的基因组，并在压缩结果中附加 FASTA/Q 注释（例如 BC:Z:CGTAC）：

`bwa mem -C -t 32 {{path/to/reference.fa}} {{path/to/read_pair_end_1.fq.gz}} {{path/to/read_pair_end_2.fq.gz}} | gzip > {{path/to/alignment_pair_end.sam.gz}}`