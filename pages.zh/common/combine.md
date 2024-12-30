# 合并

> 对两个文件的行执行集合操作。
> 输出行的顺序由第一个文件中的行的顺序决定。
> 另见：`diff`。
> 更多信息：<https://joeyh.name/code/moreutils/>.

- 输出在两个指定文件中都存在的行：

`combine {{path/to/file1}} 和 {{path/to/file2}}`

- 输出在第一个文件中但不在第二个文件中的行：

`combine {{path/to/file1}} 不 {{path/to/file2}}`

- 输出在任一指定文件中存在的行：

`combine {{path/to/file1}} 或 {{path/to/file2}}`

- 输出仅在一个指定文件中存在的行：

`combine {{path/to/file1}} 异或 {{path/to/file2}}`