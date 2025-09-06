# git status

> 展示 Git 仓库中文件的变更情况。
> 列出与当前检出提交相比有修改、新增和删除的文件。
> 更多信息：<https://git-scm.com/docs/git-status>.

- 显示修改过但尚未暂存（以备提交）的文件：

`git status`

- 以简短形式输出：

`git status {{[-s|--short]}}`

- 显示暂存区与工作目录的详细变更信息：

`git status {{[-vv|--verbose --verbose]}}`

- 显示当前分支及其跟踪（上游）分支信息：

`git status {{[-b|--branch]}}`

- 以简短形式输出，同时包含分支信息：

`git status {{[-sb|--short --branch]}}`

- 显示当前贮藏区（stash）中的条目数量：

`git status --show-stash`

- 不显示未跟踪的文件：

`git status {{[-uno|--untracked-files=no]}}`
