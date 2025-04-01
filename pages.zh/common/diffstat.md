# diffstat

> 从 `diff` 命令的输出创建直方图。
> 更多信息：<https://manned.org/diffstat>.

- 以直方图形式显示更改：

`diff {{path/to/file1}} {{path/to/file2}} | diffstat`

- 以表格形式显示插入、删除和修改的更改：

`diff {{path/to/file1}} {{path/to/file2}} | diffstat -t`
