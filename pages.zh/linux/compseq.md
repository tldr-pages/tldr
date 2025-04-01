# compseq

> 计算序列中唯一单词的组成。
> 更多信息：<https://www.bioinformatics.nl/cgi-bin/emboss/help/compseq/>.

- 统计 FASTA 文件中单词的出现频率，通过交互式提示提供参数值：

`compseq {{path/to/file.fasta}}`

- 统计 FASTA 文件中氨基酸对的出现频率，将输出保存到文本文件中：

`compseq {{path/to/input_protein.fasta}} -word 2 {{path/to/output_file.comp}}`

- 统计 FASTA 文件中六核苷酸的出现频率，将输出保存到文本文件中，并忽略零计数：

`compseq {{path/to/input_dna.fasta}} -word 6 {{path/to/output_file.comp}} -nozero`

- 在特定的阅读框中统计密码子的出现频率；忽略任何重叠计数（即以单词长度 3 移动窗口）：

`compseq -sequence {{path/to/input_rna.fasta}} -word 3 {{path/to/output_file.comp}} -nozero -frame {{1}}`

- 统计密码子在向后移动 3 个位置的阅读框中的出现频率；忽略任何重叠计数（应报告除第一个密码子外的所有密码子）：

`compseq -sequence {{path/to/input_rna.fasta}} -word 3 {{path/to/output_file.comp}} -nozero -frame 3`

- 统计 FASTA 文件中的三联氨基酸，并与 `compseq` 的先前运行结果比较以计算预期和标准化频率值：

`compseq -sequence {{path/to/human_proteome.fasta}} -word 3 {{path/to/output_file1.comp}} -nozero -infile {{path/to/output_file2.comp}}`

- 通过使用提供的输入序列中的单个碱基/残基频率来计算预期频率，从而近似上述命令，而无需预先准备的文件：

`compseq -sequence {{path/to/human_proteome.fasta}} -word 3 {{path/to/output_file.comp}} -nozero -calcfreq`

- 显示帮助（使用 `-help -verbose` 以获得更多关于相关和通用限定符的信息）：

`compseq -help`
