# stat

> 显示文件和文件系统信息。
> 另请参阅：`file`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>。

- 显示文件的属性，如大小、权限、创建日期和访问日期等：

`stat {{路径/到/文件}}`

- 显示文件的属性，仅显示原始结果数据，不显示标签：

`stat {{[-t|--terse]}} {{路径/到/文件}}`

- 显示文件所在文件系统的信息：

`stat {{[-f|--file-system]}} {{路径/到/文件}}`

- 仅显示八进制文件权限：

`stat {{[-c|--format]}} "%a %n" {{路径/到/文件}}`

- 显示文件的所有者和组：

`stat {{[-c|--format]}} "%U %G" {{路径/到/文件}}`

- 以字节为单位显示文件大小：

`stat {{[-c|--format]}} "%s %n" {{路径/到/文件}}`
