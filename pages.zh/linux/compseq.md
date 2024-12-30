# compseq

> 计算序列中唯一单词的组成。
> 更多信息：<https://www.bioinformatics.nl/cgi-bin/emboss/help/compseq/>.

- 计算FASTA文件中单词的观察频率，提供交互提示的参数值：

`compseq {{path/to/file.fasta}}`

- 从FASTA文件中计算氨基酸对的观察频率，并将输出保存到文本文件中：

`compseq {{path/to/input_protein.fasta}} -word 2 {{path/to/output_file.comp}}`

- 从FASTA文件中计算六聚核苷酸的观察频率，并将输出保存到文本文件中，同时忽略零计数：

`compseq {{path/to/input_dna.fasta}} -word 6 {{path/to/output_file.comp}} -nozero`

- 计算特定阅读框中的密码子的观察频率；忽略任何重叠计数（即按单词长度3移动窗口）：

`compseq -sequence {{path/to/input_rna.fasta}} -word 3 {{path/to/output_file.comp}} -nozero -frame {{1}}`

- 计算密码子向右移位3个位置的观察频率；忽略任何重叠计数（应报告除第一个外的所有密码子）：

`compseq -sequence {{path/to/input_rna.fasta}} -word 3 {{path/to/output_file.comp}} -nozero -frame 3`

- 计算FASTA文件中的氨基酸三联体，并与先前运行的`compseq`进行比较，以计算预期和标准化频率值：

`compseq -sequence {{path/to/human_proteome.fasta}} -word 3 {{path/to/output_file1.comp}} -nozero -infile {{path/to/output_file2.comp}}`

- 通过使用提供的输入序列中的单个碱基/残基频率来计算预期频率，从而近似上述命令，而无需预先准备的文件：

`compseq -sequence {{path/to/human_proteome.fasta}} -word 3 {{path/to/output_file.comp}} -nozero -calcfreq`

- 显示帮助（使用`-help -verbose`以获取更多关于相关和一般限定符的信息）：

`compseq -help`