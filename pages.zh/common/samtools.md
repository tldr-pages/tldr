# samtools

> 用于处理高通量测序（基因组学）数据的工具。
> 用于读取、写入、编辑、索引和查看 SAM/BAM/CRAM 格式的数据。
> 更多信息：<https://www.htslib.org>。

- 将 SAM 输入文件转换为 BAM 流并保存到文件中：

`samtools view -S -b {{input.sam}} > {{output.bam}}`

- 从 `stdin`（-）获取输入，并将 SAM 头信息和指定区域内的任何读取打印到 `stdout`：

`{{other_command}} | samtools view -h - chromosome:start-end`

- 对文件进行排序并保存为 BAM（输出格式根据输出文件的扩展名自动确定）：

`samtools sort {{input}} -o {{output.bam}}`

- 为排序的 BAM 文件建立索引（创建 `sorted_input.bam.bai`）：

`samtools index {{sorted_input.bam}}`

- 打印文件的比对统计数据：

`samtools flagstat {{sorted_input}}`

- 统计每个索引（染色体/连续体）的比对数量：

`samtools idxstats {{sorted_indexed_input}}`

- 合并多个文件：

`samtools merge {{output}} {{input1 input2 ...}}`

- 根据读取组拆分输入文件：

`samtools split {{merged_input}}`
