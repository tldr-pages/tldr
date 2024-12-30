# blastn

> 核苷酸-核苷酸 BLAST。
> 更多信息：<https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastn_application_options/>.

- 使用 megablast（默认）对两个或多个序列进行比对，e-value 阈值为 1e-9，成对输出格式（默认）：

`blastn -query {{query.fa}} -subject {{subject.fa}} -evalue {{1e-9}}`

- 使用 blastn 对两个或多个序列进行比对：

`blastn -task blastn -query {{query.fa}} -subject {{subject.fa}}`

- 对两个或多个序列进行比对，自定义制表输出格式，输出到文件：

`blastn -query {{query.fa}} -subject {{subject.fa}} -outfmt {{'6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident'}} -out {{output.tsv}}`

- 使用核苷酸查询在核苷酸数据库中搜索，使用 16 个线程（CPU）进行 BLAST 搜索，最多保留 10 个比对序列：

`blastn -query {{query.fa}} -db {{path/to/blast_db}} -num_threads {{16}} -max_target_seqs {{10}}`

- 使用核苷酸查询在远程非冗余核苷酸数据库中搜索：

`blastn -query {{query.fa}} -db {{nt}} -remote`

- 显示帮助（使用 `-help` 获取详细帮助）：

`blastn -h`