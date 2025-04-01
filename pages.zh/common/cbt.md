# cbt

> 用于从 Google Cloud 的 Bigtable 读取数据的工具。
> 更多信息：<https://cloud.google.com/bigtable/docs/cbt-reference>.

- 列出当前项目中的表：

`cbt ls`

- 显示当前项目中特定表的行数：

`cbt count "{{table_name}}"`

- 显示当前项目中特定表中的单行，每列仅显示最新单元格版本：

`cbt lookup "{{table_name}}" "{{row_key}}" cells-per-column={{1}}`

- 显示当前项目中特定表中的单行，仅显示指定列（省略限定符以返回整个列族）：

`cbt lookup "{{table_name}}" "{{row_key}}" columns="{{family1:qualifier1,family2:qualifier2,...}}"`

- 在当前项目中按特定正则表达式模式搜索最多 5 行并打印它们：

`cbt read "{{table_name}}" regex="{{row_key_pattern}}" count={{5}}`

- 读取当前项目中特定范围的行并仅打印返回的行键：

`cbt read {{table_name}} start={{start_row_key}} end={{end_row_key}} keys-only=true`