# git 状态

> 显示 Git 仓库中文件的更改。
> 列出与当前检出的提交相比，已更改、已添加和已删除的文件。
> 更多信息：<https://git-scm.com/docs/git-status>。

- 显示尚未添加以进行提交的更改文件：

`git status`

- 以 [s]hort 格式输出：

`git status --short`

- 显示暂存区和工作目录中更改的 [v]erbose 信息：

`git status --verbose --verbose`

- 显示 [b]ranch 和跟踪信息：

`git status --branch`

- 以 [s]hort 格式输出并带有 [b]ranch 信息：

`git status --short --branch`

- 显示当前已暂存的条目数量：

`git status --show-stash`

- 在输出中不显示未跟踪的文件：

`git status --untracked-files=no`