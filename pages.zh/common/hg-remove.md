# hg remove

> 从暂存区域移除指定的文件。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#remove>。

- 从暂存区域移除文件或目录：

`hg remove {{path/to/file}}`

- 移除所有匹配指定模式的已暂存文件：

`hg remove --include {{pattern}}`

- 移除所有已暂存文件，排除那些匹配指定模式的文件：

`hg remove --exclude {{pattern}}`

- 递归移除子仓库：

`hg remove --subrepos`

- 从仓库中移除已被物理删除的文件：

`hg remove --after`