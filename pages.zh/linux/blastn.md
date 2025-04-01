# blastn

> 核苷酸-核苷酸 BLAST。
> 更多信息：<https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastn_application_options/>.

- 使用 megablast（默认值），e-value 阈值为 1e-9，配对输出格式（默认值）比对两个或多个序列：

`blastn -query {{query.fa}} -subject {{subject.fa}} -evalue {{1e-9}}`

- 使用 blastn 比对两个或多个序列：

`blastn -task blastn -query {{query.fa}} -subject {{subject.fa}}`

- 比对两个或多个序列，自定义表格输出格式，并输出到文件：

`blastn -query {{query.fa}} -subject {{subject.fa}} -outfmt {{'6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident'}} -out {{output.tsv}}`

- 使用核苷酸查询搜索核苷酸数据库，使用 16 个线程（CPU）进行 BLAST 搜索，最多保留 10 个对齐序列：

`blastn -query {{query.fa}} -db {{path/to/blast_db}} -num_threads {{16}} -max_target_seqs {{10}}`

- 使用核苷酸查询远程搜索非冗余核苷酸数据库：

`blastn -query {{query.fa}} -db {{nt}} -remote`

- 显示帮助（使用 `-help` 显示详细帮助）：

`blastn -h`
