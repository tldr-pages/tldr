# svn

> Subversion 命令行客户端工具。
> 更多信息：<https://subversion.apache.org>。

- 从仓库中检出一个工作副本：

`svn co {{url/to/repository}}`

- 将仓库中的更改同步到工作副本：

`svn up`

- 将文件和目录置于版本控制下，计划将其添加到仓库中。这些文件将在下次提交时添加：

`svn add {{PATH}}`

- 将工作副本中的更改提交到仓库：

`svn ci -m {{commit_log_message}} [{{PATH}}]`

- 显示最近 10 次修订的更改，显示每次修订的修改文件：

`svn log -vl {{10}}`

- 显示帮助信息：

`svn help`
