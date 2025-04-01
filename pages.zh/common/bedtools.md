# bedtools

> 基因组分析任务的多功能工具集。
> 用于处理BAM、BED、GFF/GTF、VCF格式的数据，进行数据的交集、分组、转换和计数。
> 更多信息：<https://bedtools.readthedocs.io/en/latest/content/overview.html#summary-of-available-tools>.

- 根据序列的链方向 [s] 交集文件 [a] 和文件 [b]，并将结果保存到特定文件中：

`bedtools intersect -a {{path/to/file_A}} -b {{path/to/file_B1 path/to/file_B2 ...}} -s > {{path/to/output_file}}`

- 以左外连接 [l] [o] [j] 方式交集两个文件，即报告 `file1` 中的每个特征，如果没有与 `file2` 重叠则报告 NULL：

`bedtools intersect -a {{path/to/file1}} -b {{path/to/file2}} -loj > {{path/to/output_file}}`

- 使用更高效的算法交集中两个预排序的文件：

`bedtools intersect -a {{path/to/file1}} -b {{path/to/file2}} -sorted > {{path/to/output_file}}`

- 根据文件的前三个和第五个 [c] 列 [g] 分组，并对第六列应用求和 [o] 操作：

`bedtools groupby -i {{path/to/file}} -c 1-3,5 -g 6 -o sum`

- 将 bam 格式的 [i] 输入文件转换为 bed 格式的文件：

`bedtools bamtobed -i {{path/to/file.bam}} > {{path/to/file.bed}}`

- 为 `file1.bed` 中的所有特征找到 `file2.bed` 中最近的特征，并在额外的列中写入它们的 [d] 距离（输入文件必须排序）：

`bedtools closest -a {{path/to/file1.bed}} -b {{path/to/file2.bed}} -d`