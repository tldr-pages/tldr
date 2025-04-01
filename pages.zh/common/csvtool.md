# csvtool

> 用于从 CSV 格式的数据源中过滤和提取数据的工具。
> 更多信息：<https://github.com/maroofi/csvtool>.

- 从 CSV 文件中提取第二列：

`csvtool --column {{2}} {{path/to/file.csv}}`

- 从 CSV 文件中提取第二列和第四列：

`csvtool --column {{2,4}} {{path/to/file.csv}}`

- 从 CSV 文件中提取第二列完全匹配 'Foo' 的行：

`csvtool --column {{2}} --search '{{^Foo$}}' {{path/to/file.csv}}`

- 从 CSV 文件中提取第二列以 'Bar' 开头的行：

`csvtool --column {{2}} --search '{{^Bar}}' {{path/to/file.csv}}`

- 在 CSV 文件中查找第二列以 'Baz' 结尾的行，然后提取第三列和第六列：

`csvtool --column {{2}} --search '{{Baz$}}' {{path/to/file.csv}} | csvtool --no-header --column {{3,6}}`
