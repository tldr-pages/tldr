# blastp

> 蛋白质-蛋白质 BLAST。
> 更多信息：<https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastp_application_options/>.

- 使用 blastp 对两个或多个序列进行比对，E 值阈值为 1e-9，配对输出格式，输出到屏幕：

`blastp -query {{query.fa}} -subject {{subject.fa}} -evalue {{1e-9}}`

- 使用 blastp-fast 对两个或多个序列进行比对：

`blastp -task blastp-fast -query {{query.fa}} -subject {{subject.fa}}`

- 对两个或多个序列进行比对，自定义表格输出格式，输出到文件：

`blastp -query {{query.fa}} -subject {{subject.fa}} -outfmt '{{6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident}}' -out {{output.tsv}}`

- 使用蛋白质查询搜索蛋白质数据库，BLAST 搜索使用 16 个线程，最多保留 10 个比对序列：

`blastp -query {{query.fa}} -db {{blast_database_name}} -num_threads {{16}} -max_target_seqs {{10}}`

- 使用蛋白质查询搜索远程非冗余蛋白质数据库：

`blastp -query {{query.fa}} -db {{nr}} -remote`

- 显示帮助（使用 `-help` 以获取详细帮助）：

`blastp -h`