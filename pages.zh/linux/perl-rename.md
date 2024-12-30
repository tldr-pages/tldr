# 重命名

> 重命名多个文件。
> 注意：此页面指的是 `perl-rename` Arch Linux 包中的命令。
> 更多信息：<https://manned.org/rename>。

- 使用 Perl 常见正则表达式重命名文件（将 'foo' 替换为 'bar'）：

`rename {{'s/foo/bar/'}} {{*}}`

- 干运行 - 显示将会进行的重命名，但不实际执行：

`rename -n {{'s/foo/bar/'}} {{*}}`

- 强制重命名，即使操作会删除现有的目标文件：

`rename -f {{'s/foo/bar/'}} {{*}}`

- 将文件名转换为小写（在不区分大小写的文件系统中使用 `-f` 以防止“已存在”错误）：

`rename 'y/A-Z/a-z/' {{*}}`

- 用下划线替换空格：

`rename 's/\s+/_/g' {{*}}`