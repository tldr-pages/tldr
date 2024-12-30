# csv2tsv

> 将CSV（以逗号分隔）文本转换为TSV（以制表符分隔）格式。  
> 更多信息：<https://github.com/eBay/tsv-utils/blob/master/README.md#csv2tsv>。

- 从CSV转换为TSV：

`csv2tsv {{path/to/input_csv1 path/to/input_csv2 ...}} > {{path/to/output_tsv}}`

- 将以字段分隔符分隔的CSV转换为TSV：

`csv2tsv -c'{{field_delimiter}}' {{path/to/input_csv}}`

- 将以分号分隔的CSV转换为TSV：

`csv2tsv -c';' {{path/to/input_csv}}`