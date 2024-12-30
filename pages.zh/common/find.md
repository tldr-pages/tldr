# 查找

> 在目录树下递归查找文件或目录。
> 更多信息：<https://manned.org/find>。

- 按扩展名查找文件：

`find {{root_path}} -name '{{*.ext}}'`

- 查找匹配多个路径/名称模式的文件：

`find {{root_path}} -path '{{**/path/**/*.ext}}' -or -name '{{*pattern*}}'`

- 以不区分大小写的模式查找匹配给定名称的目录：

`find {{root_path}} -type d -iname '{{*lib*}}'`

- 查找匹配给定模式的文件，排除特定路径：

`find {{root_path}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- 查找匹配给定大小范围的文件，将递归深度限制为“1”：

`find {{root_path}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- 对每个文件运行一个命令（在命令中使用 `{}` 访问文件名）：

`find {{root_path}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- 查找今天修改的所有文件并将结果作为参数传递给单个命令：

`find {{root_path}} -daystart -mtime {{-1}} -exec {{tar -cvf archive.tar}} {} \+`

- 查找空文件（0字节）或目录并详细删除它们：

`find {{root_path}} -type {{f|d}} -empty -delete -print`