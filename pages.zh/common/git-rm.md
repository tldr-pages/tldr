# git rm

> 从仓库索引和本地文件系统中移除文件。
> 更多信息：<https://git-scm.com/docs/git-rm>.

- 从仓库索引和文件系统中移除文件：

`git rm {{path/to/file}}`

- 从仓库索引和文件系统中移除目录：

`git rm -r {{path/to/directory}}`

- 从仓库索引中移除文件，但保留其在本地的副本：

`git rm --cached {{path/to/file}}`