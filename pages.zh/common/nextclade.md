# nextclade

> 生物信息学工具，用于病毒基因组比对、世系分组和质量控制检查。
> 更多信息：<https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli/reference.html>.

- 将序列比对到用户提供的参考序列，并将比对结果输出到文件：

`nextclade run {{path/to/sequences.fa}} {{[-r|--input-ref]}} {{path/to/reference.fa}} {{[-o|--output-fasta]}} {{path/to/alignment.fa}}`

- 创建一个 TSV 报告，自动下载最新数据集：

`nextclade run {{path/to/fasta}} {{[-d|--dataset-name]}} {{dataset_name}} {{[-t|--output-tsv]}} {{path/to/report.tsv}}`

- 列出所有可用的数据集：

`nextclade dataset list`

- 下载最新的 SARS-CoV-2 数据集：

`nextclade dataset get {{[-n|--name]}} sars-cov-2 {{[-o|--output-dir]}} {{path/to/directory}}`

- 使用已下载的数据集，生成所有输出：

`nextclade run {{[-D|--input-dataset]}} {{path/to/dataset_dir}} {{[-O|--output-all]}} {{path/to/output_dir}} {{path/to/sequences.fasta}}`

- 在多个文件上运行：

`nextclade run {{[-d|--dataset-name]}} {{dataset_name}} {{[-t|--output-tsv]}} {{path/to/output_tsv}} -- {{path/to/input_fasta_1 path/to/input_fasta_2 ...}}`

- 如果序列不能比对，尝试反向互补：

`nextclade run --retry-reverse-complement {{[-d|--dataset-name]}} {{dataset_name}} {{[-t|--output-tsv]}} {{path/to/output_tsv}} {{path/to/input_fasta}}`