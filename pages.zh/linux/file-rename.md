# rename

> 重命名多个文件。
> 注意：此页指的是来自 `rename` Debian 软件包的命令。
> 更多信息：<https://manned.org/file-rename>.

- 使用 Perl 常规正则表达式重命名文件（将出现的所有 'foo' 替换为 'bar'）：

`rename {{'s/foo/bar/'}} {{*}}`

- 模拟运行 - 显示将要进行的重命名操作但不执行：

`rename -n {{'s/foo/bar/'}} {{*}}`

- 强制重命名，即使操作会导致删除已存在的目标文件：

`rename -f {{'s/foo/bar/'}} {{*}}`

- 将文件名转换为小写（在不区分大小写的文件系统中使用 `-f` 以防止“文件已存在”错误）：

`rename 'y/A-Z/a-z/' {{*}}`

- 将空格替换为下划线：

`rename 's/\s+/_/g' {{*}}`