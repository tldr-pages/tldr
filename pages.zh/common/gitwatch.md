# gitwatch

> 自动将文件或目录的更改提交到 Git 仓库。
> 更多信息：<https://github.com/gitwatch/gitwatch>。

- 自动提交对文件或目录所做的任何更改：

`gitwatch {{path/to/file_or_directory}}`

- 自动提交更改并将其推送到远程仓库：

`gitwatch -r {{remote_name}} {{path/to/file_or_directory}}`

- 自动提交更改并将其推送到远程仓库的特定分支：

`gitwatch -r {{remote_name}} -b {{branch_name}} {{path/to/file_or_directory}}`