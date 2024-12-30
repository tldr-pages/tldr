# wdiff

> 显示文本文件之间的单词差异。
> 更多信息：<https://www.gnu.org/software/wdiff/>.

- 比较两个文件：

`wdiff {{path/to/file1}} {{path/to/file2}}`

- 比较时忽略大小写：

`wdiff --ignore-case {{path/to/file1}} {{path/to/file2}}`

- 显示删除、插入或替换了多少个单词：

`wdiff --statistics {{path/to/file1}} {{path/to/file2}}`