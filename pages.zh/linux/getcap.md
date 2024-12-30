# getcap

> 显示每个指定文件的名称和能力的命令。
> 更多信息：<https://manned.org/getcap>。

- 获取给定文件的能力：

`getcap {{path/to/file1 path/to/file2 ...}}`

- 递归获取给定目录下所有文件的能力：

`getcap -r {{path/to/directory1 path/to/directory2 ...}}`

- 即使没有设置能力，也显示所有搜索的条目：

`getcap -v {{path/to/file1 path/to/file2 ...}}`