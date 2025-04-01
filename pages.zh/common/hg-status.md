# hg status

> 显示工作目录中已更改的文件。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#status>.

- 显示已更改文件的状态：

`hg status`

- 仅显示已修改的文件：

`hg status --modified`

- 仅显示已添加的文件：

`hg status --added`

- 仅显示已删除的文件：

`hg status --removed`

- 仅显示已标记为删除（但仍在跟踪）的文件：

`hg status --deleted`

- 显示工作目录中相对于指定修订版本的更改：

`hg status --rev {{revision}}`

- 仅显示匹配指定通配符模式的文件：

`hg status --include {{pattern}}`

- 显示文件，排除匹配指定通配符模式的文件：

`hg status --exclude {{pattern}}`
