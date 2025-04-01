# hg add

> 将指定文件添加到 Mercurial 下一次提交的暂存区。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#add>。

- 将文件或目录添加到暂存区：

`hg add {{path/to/file}}`

- 将匹配指定模式的所有未暂存文件添加到暂存区：

`hg add --include {{pattern}}`

- 将所有未暂存文件添加到暂存区，但排除匹配指定模式的文件：

`hg add --exclude {{pattern}}`

- 递归添加子仓库：

`hg add --subrepos`

- 执行测试运行，但不执行任何实际操作：

`hg add --dry-run`