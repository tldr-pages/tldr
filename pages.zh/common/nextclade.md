# nextclade

> 用于病毒基因组比对、谱系分配和质量检查的生物信息学工具。
> 更多信息：<https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli/index.html>。

- 将序列比对到用户提供的[r]eference，并将比对结果输出到文件：

`nextclade run {{path/to/sequences.fa}} -r {{path/to/reference.fa}} -o {{path/to/alignment.fa}}`

- 创建[t]SV报告，自动下载最新[d]ataset：

`nextclade run {{path/to/fasta}} -d {{dataset_name}} -t {{path/to/report.tsv}}`

- 列出所有可用的数据集：

`nextclade dataset list`

- 下载最新的SARS-CoV-2数据集：

`nextclade dataset get --name sars-cov-2 --output-dir {{path/to/directory}}`

- 使用下载的数据集[D]ataset，生成所有[O]utputs：

`nextclade run -D {{path/to/dataset_dir}} -O {{path/to/output_dir}} {{path/to/sequences.fasta}}`

- 在多个文件上运行：

`nextclade run -d {{dataset_name}} -t {{path/to/output_tsv}} -- {{path/to/input_fasta_1 path/to/input_fasta_2 ...}}`

- 如果序列未能比对，尝试反向互补：

`nextclade run --retry-reverse-complement -d {{dataset_name}} -t {{path/to/output_tsv}} {{path/to/input_fasta}}`