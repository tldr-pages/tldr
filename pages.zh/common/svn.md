# svn

> Subversion 命令行客户端工具。
> 更多信息：<https://subversion.apache.org>。

- 从版本库检出工作副本：

`svn co {{url/to/repository}}`

- 将版本库中的更改带入工作副本：

`svn up`

- 将文件和目录置于版本控制下，安排它们添加到版本库。它们将在下次提交中被添加：

`svn add {{PATH}}`

- 将工作副本中的更改发送到版本库：

`svn ci -m {{commit_log_message}} [{{PATH}}]`

- 显示最近 10 次修订的更改，显示每次修订的修改文件：

`svn log -vl {{10}}`

- 显示帮助信息：

`svn help`