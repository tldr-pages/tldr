# find

> 在指定目录树下递归查找文件或目录。
> 更多信息：<https://manned.org/find>.

- 通过扩展名查找文件：

`find {{指定目录}} -name '{{*.ext}}'`

- 查找匹配多个路径或名称模式的文件：

`find {{指定目录}} -path '{{**/path/**/*.ext}}' -or -name '{{*pattern*}}'`

- 查找匹配指定名称的目录，不区分大小写：

`find {{指定目录}} -type d -iname '{{*lib*}}'`

- 查找匹配指定模式的文件，排除特定路径：

`find {{指定目录}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- 查找符合指定大小范围的文件：

`find {{指定目录}} -size {{+500k}} -size {{-10M}}`

- 对每个文件运行命令（在命令中使用 `{}` 代表当前文件）：

`find {{指定目录}} -name '{{*.ext}}' -exec {{wc -l {} }}\;`

- 查找最近 7 天修改的文件并删除：

`find {{指定目录}} -daystart -mtime -{{7}} -delete`

- 查找空（0 字节）的文件并删除：

`find {{指定目录}} -type {{f}} -empty -delete`
