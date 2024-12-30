# samtools

> 处理高通量测序（基因组学）数据的工具。
> 用于读取/写入/编辑/索引/查看SAM/BAM/CRAM格式的数据。
> 更多信息：<https://www.htslib.org>。

- 将SAM输入文件转换为BAM流并保存到文件：

`samtools view -S -b {{input.sam}} > {{output.bam}}`

- 从`stdin`（-）获取输入，并将SAM头和任何与特定区域重叠的读取打印到`stdout`：

`{{other_command}} | samtools view -h - chromosome:start-end`

- 对文件进行排序并保存为BAM（输出格式会根据输出文件的扩展名自动确定）：

`samtools sort {{input}} -o {{output.bam}}`

- 为已排序的BAM文件建立索引（创建`sorted_input.bam.bai`）：

`samtools index {{sorted_input.bam}}`

- 打印文件的比对统计信息：

`samtools flagstat {{sorted_input}}`

- 计算每个索引（染色体/连锁群）的比对数：

`samtools idxstats {{sorted_indexed_input}}`

- 合并多个文件：

`samtools merge {{output}} {{input1 input2 ...}}`

- 根据读取组拆分输入文件：

`samtools split {{merged_input}}`