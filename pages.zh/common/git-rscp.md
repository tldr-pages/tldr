# git rscp

> 反向 `git scp` - 从远程仓库的工作目录复制文件到当前工作树。
> 这是 `git-extras` 的一部分。
> 更多信息： <https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>。

- 从远程复制特定文件：

`git rscp {{remote_name}} {{path/to/file1 path/to/file2 ...}}`

- 从远程复制特定目录：

`git rscp {{remote_name}} {{path/to/directory}}`