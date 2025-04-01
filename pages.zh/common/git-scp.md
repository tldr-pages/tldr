# git scp

> 从当前工作树复制文件到远程仓库的工作目录。
> 属于 `git-extras`。使用 `rsync` 传输文件。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>。

- 复制未暂存的文件到指定的远程：

`git scp {{remote_name}}`

- 复制已暂存和未暂存的文件到远程：

`git scp {{remote_name}} HEAD`

- 复制最后一次提交中更改的文件以及任何已暂存或未暂存的文件到远程：

`git scp {{remote_name}} HEAD~1`

- 复制特定的文件到远程：

`git scp {{remote_name}} {{path/to/file1 path/to/file2 ...}}`

- 复制特定的目录到远程：

`git scp {{remote_name}} {{path/to/directory}}`
