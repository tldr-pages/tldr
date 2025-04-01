# csv2tsv

> 将 CSV（逗号分隔）文本转换为 TSV（制表符分隔）格式。
> 更多信息：<https://github.com/eBay/tsv-utils/blob/master/README.md#csv2tsv>.

- 将 CSV 转换为 TSV：

`csv2tsv {{path/to/input_csv1 path/to/input_csv2 ...}} > {{path/to/output_tsv}}`

- 将其他分隔符分隔的 CSV 转换为 TSV：

`csv2tsv -c'{{field_delimiter}}' {{path/to/input_csv}}`

- 将分号分隔的 CSV 转换为 TSV：

`csv2tsv -c';' {{path/to/input_csv}}`
