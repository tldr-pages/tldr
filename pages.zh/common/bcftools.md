# bcftools

> 用于操作 VCF 和 BCF 文件的工具。
> 更多信息：<https://samtools.github.io/bcftools/bcftools.html>。

- 查看 BCF 文件并转换为 VCF 输出到 `stdout`：

`bcftools view {{路径/到/input.bcf}} {{[-O|--output-type]}} v`

- 按染色体和位置对 VCF 文件变异进行排序，输出到 BCF 文件，并对排序后的输出建立索引：

`bcftools sort {{路径/到/input.vcf.gz}} {{[-O|--output-type]}} b {{[-o|--output]}} {{路径/到/sorted.bcf}} {{[-W|--write-index]}}`

- 将共享相同样本的已排序 VCF 文件连接为压缩 VCF 输出到 `stdout`：

`bcftools concat {{路径/到/chr1.vcf.gz 路径/到/chr2.vcf.gz ...}} {{[-O|--output-type]}} z`

- 过滤低质量变异并在 FILTER 列中标注 "LowQual" 标签：

`bcftools filter {{[-e|--exclude]}} 'QUAL<20' {{[-s|--soft-filter]}} LowQual {{路径/到/input.vcf.gz}}`

- 从 tabix 索引表添加注释列到 `stdout`：

`bcftools annotate {{[-a|--annotations]}} {{路径/到/annotations.tsv.gz}} {{[-c|--columns]}} CHROM,POS,REF,ALT,INFO/AF {{路径/到/input.vcf.gz}}`

- 使用 4 个线程输出 VCF 文件之间的变异交集：

`bcftools isec {{路径/到/a.vcf.gz 路径/到/b.vcf.gz ...}} --threads 4 {{[-o|--output]}} {{路径/到/intersection.vcf}}`

- 合并没有索引的 VCF 文件中的非重叠样本到 `stdout`：

`bcftools merge {{路径/到/cohort1.vcf.gz}} {{路径/到/cohort2.vcf.gz}} --no-index`

- 为 bgzipped VCF 文件创建索引：

`bcftools index {{路径/到/input.vcf.gz}}`
