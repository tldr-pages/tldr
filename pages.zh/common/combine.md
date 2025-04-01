# combine

> 对两个文件的行执行集合操作。
> 输出行的顺序由第一个文件中的行顺序决定。
> 另见：`diff`。
> 更多信息：<https://joeyh.name/code/moreutils/>。

- 输出两个指定文件中共有的行：

`combine {{path/to/file1}} and {{path/to/file2}}`

- 输出在第一个文件中但不在第二个文件中的行：

`combine {{path/to/file1}} not {{path/to/file2}}`

- 输出在任意一个指定文件中的行：

`combine {{path/to/file1}} or {{path/to/file2}}`

- 输出在恰好一个指定文件中的行：

`combine {{path/to/file1}} xor {{path/to/file2}}`