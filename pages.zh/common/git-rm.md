# git rm

> 从仓库索引和本地文件系统中删除文件。
> 更多信息：<https://git-scm.com/docs/git-rm>。

- 从仓库索引和文件系统中删除文件：

`git rm {{path/to/file}}`

- 删除目录：

`git rm -r {{path/to/directory}}`

- 从仓库索引中删除文件，但在本地保持不变：

`git rm --cached {{path/to/file}}`