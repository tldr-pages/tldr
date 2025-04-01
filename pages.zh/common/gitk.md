# gitk

> 以图形方式浏览 Git 仓库。
> 另见：`git-gui`，`git-cola`，`tig`。
> 更多信息：<https://git-scm.com/docs/gitk>。

- 显示当前 Git 仓库的仓库浏览器：

`gitk`

- 显示特定文件或目录的仓库浏览器：

`gitk {{path/to/file_or_directory}}`

- 显示从 1 周前至今的提交：

`gitk --since="{{1 week ago}}"`

- 显示早于 2016 年 1 月 1 日的提交：

`gitk --until="{{1/1/2015}}"`

- 显示所有分支中最多 100 次更改：

`gitk --max-count=100 --all`