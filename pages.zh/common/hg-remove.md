# hg remove

> 从暂存区中移除指定的文件。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#remove>.

- 从暂存区中移除文件或目录：

`hg remove {{path/to/file}}`

- 移除所有匹配指定模式的已暂存文件：

`hg remove --include {{pattern}}`

- 移除所有已暂存的文件，但排除匹配指定模式的文件：

`hg remove --exclude {{pattern}}`

- 递归移除子仓库：

`hg remove --subrepos`

- 移除已物理删除的文件：

`hg remove --after`