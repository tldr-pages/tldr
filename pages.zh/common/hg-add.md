# hg add

> 将指定文件添加到 Mercurial 的下一个提交的暂存区。
> 更多信息：<https://www.mercurial-scm.org/doc/hg.1.html#add>。

- 将文件或目录添加到暂存区：

`hg add {{path/to/file}}`

- 添加所有与指定模式匹配的未暂存文件：

`hg add --include {{pattern}}`

- 添加所有未暂存文件，排除与指定模式匹配的文件：

`hg add --exclude {{pattern}}`

- 递归添加子仓库：

`hg add --subrepos`

- 执行测试运行而不执行任何操作：

`hg add --dry-run`