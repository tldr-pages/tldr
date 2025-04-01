# git ignore

> 显示/更新 `.gitignore` 文件。
> 属于 `git-extras`。另见 `git ignore-io`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-ignore>。

- 显示所有全局和本地 `.gitignore` 文件的内容：

`git ignore`

- 私下忽略文件，更新 `.git/info/exclude` 文件：

`git ignore {{file_pattern}} --private`

- 本地忽略文件，更新本地 `.gitignore` 文件：

`git ignore {{file_pattern}}`

- 全局忽略文件，更新全局 `.gitignore` 文件：

`git ignore {{file_pattern}} --global`
