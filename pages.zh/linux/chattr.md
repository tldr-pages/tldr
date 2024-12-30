# chattr

> 更改文件或目录的属性。
> 更多信息：<https://manned.org/chattr>。

- 使文件或目录对更改和删除不可变，即使是超级用户也不能更改：

`chattr +i {{path/to/file_or_directory}}`

- 使文件或目录可变：

`chattr -i {{path/to/file_or_directory}}`

- 递归地使整个目录及其内容不可变：

`chattr -R +i {{path/to/directory}}`