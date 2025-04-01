# chattr

> 更改文件或目录的属性。
> 更多信息：<https://manned.org/chattr>.

- 使文件或目录不可更改和删除，即使是超级用户也无法修改：

`chattr +i {{path/to/file_or_directory}}`

- 使文件或目录可更改：

`chattr -i {{path/to/file_or_directory}}`

- 递归地使整个目录及其内容不可更改：

`chattr -R +i {{path/to/directory}}`
