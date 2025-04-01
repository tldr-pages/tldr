# git mv

> 移动或重命名文件并更新 Git 索引。
> 更多信息：<https://git-scm.com/docs/git-mv>.

- 在仓库内移动文件，并将移动操作添加到下次提交中：

`git mv {{path/to/file}} {{new/path/to/file}}`

- 重命名文件或目录，并将重命名操作添加到下次提交中：

`git mv {{path/to/file_or_directory}} {{path/to/destination}}`

- 如果目标路径已存在文件或目录，则覆盖它：

`git mv --force {{path/to/file_or_directory}} {{path/to/destination}}`
