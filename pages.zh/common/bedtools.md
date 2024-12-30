# bedtools

> 一款用于基因组分析任务的瑞士军刀工具。
> 用于交集、分组、转换和计数 BAM、BED、GFF/GTF、VCF 格式的数据。
> 更多信息：<https://bedtools.readthedocs.io>。

- 根据序列的 [s]trand 交集文件 [a] 和文件 [b]，并将结果保存到特定文件中：

`bedtools intersect -a {{path/to/file_A}} -b {{path/to/file_B1 path/to/file_B2 ...}} -s > {{path/to/output_file}}`

- 使用 [l]eft [o]uter [j]oin 交集两个文件，即报告 `file1` 中的每个特征，如果与 `file2` 没有重叠则返回 NULL：

`bedtools intersect -a {{path/to/file1}} -b {{path/to/file2}} -loj > {{path/to/output_file}}`

- 使用更高效的算法交集两个预排序的文件：

`bedtools intersect -a {{path/to/file1}} -b {{path/to/file2}} -sorted > {{path/to/output_file}}`

- 根据前面三列和第五列 [c]olumn 对文件进行 [g]roup，并对第六列应用求和 [o]peration：

`bedtools groupby -i {{path/to/file}} -c 1-3,5 -g 6 -o sum`

- 将 bam 格式的 [i]nput 文件转换为 bed 格式的文件：

`bedtools bamtobed -i {{path/to/file.bam}} > {{path/to/file.bed}}`

- 在 `file1.bed` 中寻找所有特征与 `file2.bed` 中最近的一个，并在额外的列中写入它们的 [d]istance（输入文件必须已排序）：

`bedtools closest -a {{path/to/file1.bed}} -b {{path/to/file2.bed}} -d`