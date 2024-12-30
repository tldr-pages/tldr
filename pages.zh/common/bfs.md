# bfs

> 用于你的文件的广度优先搜索。
> 更多信息：<https://manned.org/bfs>。

- 通过扩展名查找文件：

`bfs {{root_path}} -name '{{*.ext}}'`

- 查找匹配多个路径/名称模式的文件：

`bfs {{root_path}} -path '{{**/path/**/*.ext}}' -or -name '{{*pattern*}}'`

- 查找匹配给定名称的目录，忽略大小写：

`bfs {{root_path}} -type d -iname '{{*lib*}}'`

- 查找匹配给定模式的文件，排除特定路径：

`bfs {{root_path}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- 查找匹配给定大小范围的文件，限制递归深度为“1”：

`bfs {{root_path}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- 对每个文件运行一个命令（在命令中使用 `{}` 以访问文件名）：

`bfs {{root_path}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- 查找今天修改的所有文件，并将结果作为参数传递给单个命令：

`bfs {{root_path}} -daystart -mtime {{-1}} -exec {{tar -cvf archive.tar}} {} \+`

- 查找空文件（0字节）或目录，并详细删除它们：

`bfs {{root_path}} -type {{f|d}} -empty -delete -print`