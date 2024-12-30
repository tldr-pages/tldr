# cbt

> 用于从 Google Cloud 的 Bigtable 中读取数据的工具。
> 更多信息请访问：<https://cloud.google.com/bigtable/docs/cbt-reference>。

- 列出当前项目中的表：

`cbt ls`

- 打印当前项目中特定表的行数：

`cbt count "{{table_name}}"`

- 从当前项目中的特定表中显示单行，仅显示每列的 1 个（最新）单元格修订：

`cbt lookup "{{table_name}}" "{{row_key}}" cells-per-column={{1}}`

- 在当前项目中显示单行，仅显示特定列（省略限定符以返回整个列族）：

`cbt lookup "{{table_name}}" "{{row_key}}" columns="{{family1:qualifier1,family2:qualifier2,...}}"`

- 根据特定的正则表达式模式在当前项目中搜索最多 5 行并打印它们：

`cbt read "{{table_name}}" regex="{{row_key_pattern}}" count={{5}}`

- 读取特定范围的行，并仅打印返回的行键，在当前项目中：

`cbt read {{table_name}} start={{start_row_key}} end={{end_row_key}} keys-only=true`