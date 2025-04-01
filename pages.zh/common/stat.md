# stat

> 显示文件和文件系统信息。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>。

- 显示特定文件的属性，如大小、权限、创建和访问日期等：

`stat {{path/to/file}}`

- 不带标签显示特定文件的属性，如大小、权限、创建和访问日期等：

`stat {{[-t|--terse]}} {{path/to/file}}`

- 显示特定文件所在文件系统的信息：

`stat {{[-f|--file-system]}} {{path/to/file}}`

- 仅显示文件的八进制权限：

`stat {{[-c|--format]}} "%a %n" {{path/to/file}}`

- 显示特定文件的所有者和组：

`stat {{[-c|--format]}} "%U %G" {{path/to/file}}`

- 显示特定文件的大小（以字节为单位）：

`stat {{[-c|--format]}} "%s %n" {{path/to/file}}`
