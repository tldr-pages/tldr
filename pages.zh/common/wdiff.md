# wdiff

> 显示文本文件之间的单词差异。
> 更多信息：<https://www.gnu.org/software/wdiff/manual/html_node/wdiff-invocation.html#wdiff-invocation>。

- 比较两个文件：

`wdiff {{path/to/file1}} {{path/to/file2}}`

- 比较时忽略大小写：

`wdiff {{[-i|--ignore-case]}} {{path/to/file1}} {{path/to/file2}}`

- 显示删除、插入或替换了多少个单词：

`wdiff {{[-s|--statistics]}} {{path/to/file1}} {{path/to/file2}}`