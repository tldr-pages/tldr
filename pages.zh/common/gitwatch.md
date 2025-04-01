# gitwatch

> 自动提交文件或目录的更改到 Git 仓库。
> 更多信息：<https://github.com/gitwatch/gitwatch>.

- 自动提交文件或目录的任何更改：

`gitwatch {{path/to/file_or_directory}}`

- 自动提交更改并推送到远程仓库：

`gitwatch -r {{remote_name}} {{path/to/file_or_directory}}`

- 自动提交更改并推送到远程仓库的指定分支：

`gitwatch -r {{remote_name}} -b {{branch_name}} {{path/to/file_or_directory}}`
