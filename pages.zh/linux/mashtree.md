# mashtree

> 从基因组生成快速树。
> 不生成系统发育树。
> 更多信息：<https://github.com/lskatz/mashtree>。

- 使用多个线程从fastq和/或fasta文件创建树的mashtree最快方法，输出到newick文件：

`mashtree --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} > {{mashtree.dnd}}`

- 使用多个线程从fastq和/或fasta文件创建树的mashtree最准确方法，输出到newick文件：

`mashtree --mindepth {{0}} --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} > {{mashtree.dnd}}`

- 创建带有置信值的树的最准确方法（请注意，任何`mashtree`本身的选项必须位于`--`的右侧）：

`mashtree_bootstrap.pl --reps {{100}} --numcpus {{12}} {{*.fastq.gz}} -- --min-depth {{0}} > {{mashtree.bootstrap.dnd}}`