# rename

> 重命名多个文件。
> 注意：此页面指的是来自 `prename` Fedora 包的命令。
> 更多信息：<https://manned.org/prename>.

- 使用 Perl 通用正则表达式重命名文件（将所有出现的 'foo' 替换为 'bar'）：

`rename {{'s/foo/bar/'}} {{*}}`

- 干运行 - 显示将要进行的重命名操作，但不执行：

`rename -n {{'s/foo/bar/'}} {{*}}`

- 强制重命名，即使该操作将删除已存在的目标文件：

`rename -f {{'s/foo/bar/'}} {{*}}`

- 将文件名转换为小写（在不区分大小写的文件系统中使用 `-f` 以防止“已存在”错误）：

`rename 'y/A-Z/a-z/' {{*}}`

- 将空格替换为下划线：

`rename 's/\s+/_/g' {{*}}`