# rename

> 重命名多个文件。
> 注意：此页面指的是 `perl-rename` Arch Linux 包中的命令。
> 更多信息：<https://manned.org/rename>.

- 使用 Perl 正则表达式重命名文件（将所有出现的 'foo' 替换为 'bar'）：

`rename {{'s/foo/bar/'}} {{*}}`

- 干运行 - 显示将要进行的重命名操作但不实际执行：

`rename -n {{'s/foo/bar/'}} {{*}}`

- 强制重命名，即使操作会删除现有的目标文件：

`rename -f {{'s/foo/bar/'}} {{*}}`

- 将文件名转换为小写（在大小写不敏感的文件系统中使用 `-f` 以避免“已存在”错误）：

`rename 'y/A-Z/a-z/' {{*}}`

- 将空格替换为下划线：

`rename 's/\s+/_/g' {{*}}`