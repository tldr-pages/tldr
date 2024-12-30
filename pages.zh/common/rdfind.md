# rdfind

> 查找具有重复内容的文件并删除它们。
> 更多信息：<https://rdfind.pauldreik.se>。

- 在给定目录中识别所有重复文件并输出摘要：

`rdfind -dryrun true {{path/to/directory}}`

- 用硬链接替换所有重复文件：

`rdfind -makehardlinks true {{path/to/directory}}`

- 用符号链接/软链接替换所有重复文件：

`rdfind -makesymlinks true {{path/to/directory}}`

- 删除所有重复文件，并且不忽略空文件：

`rdfind -deleteduplicates true -ignoreempty false {{path/to/directory}}`