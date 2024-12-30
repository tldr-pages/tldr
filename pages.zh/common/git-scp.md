# git scp

> 将文件从当前工作树复制到远程仓库的工作目录。
> 该命令是 `git-extras` 的一部分。使用 `rsync` 进行文件传输。
> 更多信息请访问：<https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>。

- 将未暂存的文件复制到指定的远程：

`git scp {{remote_name}}`

- 将已暂存和未暂存的文件复制到远程：

`git scp {{remote_name}} HEAD`

- 将上一个提交中已更改的文件以及任何已暂存或未暂存的文件复制到远程：

`git scp {{remote_name}} HEAD~1`

- 将特定文件复制到远程：

`git scp {{remote_name}} {{path/to/file1 path/to/file2 ...}}`

- 将特定目录复制到远程：

`git scp {{remote_name}} {{path/to/directory}}`