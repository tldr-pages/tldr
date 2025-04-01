# perldoc

> 查找 Perl 文档，格式为 .pod。
> 更多信息：<https://perldoc.perl.org/perldoc>。

- 查看内建 [f]unction、[v]ariable 或 [a]PI 的文档：

`perldoc -{{f|v|a}} {{name}}`

- 在 Perl FAQ 的问题标题中搜索：

`perldoc -q {{regex}}`

- 将输出直接发送到 `stdout`（默认情况下，输出会被发送到分页器）：

`perldoc -T {{page|module|program|URL}}`

- 指定所需翻译的语言代码：

`perldoc -L {{language_code}} {{page|module|program|URL}}`