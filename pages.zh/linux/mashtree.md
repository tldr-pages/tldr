# mashtree

> 从基因组快速生成树。
> 不生成系统发生树。
> 更多信息：<https://github.com/lskatz/mashtree>.

- 使用多线程从 fastq 和/或 fasta 文件中创建树的最快方法，并将结果输出到 Newick 文件：

`mashtree --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} > {{mashtree.dnd}}`

- 使用多线程从 fastq 和/或 fasta 文件中创建树的最准确方法，并将结果输出到 Newick 文件：

`mashtree --mindepth {{0}} --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} > {{mashtree.dnd}}`

- 创建带有置信值的树的最准确方法（注意任何 `mashtree` 自身的选项都必须放在 `--` 的右侧）：

`mashtree_bootstrap.pl --reps {{100}} --numcpus {{12}} {{*.fastq.gz}} -- --min-depth {{0}} > {{mashtree.bootstrap.dnd}}`
