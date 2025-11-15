# git clean

> 从工作区删除未被 Git 跟踪的文件。
> 更多信息：<https://git-scm.com/docs/git-clean>.

- 删除未跟踪的文件：

`git clean`

- 交互式删除未跟踪的文件：

`git clean {{[-i|--interactive]}}`

- 显示将被删除的文件（模拟运行，不实际删除）：

`git clean {{[-n|--dry-run]}}`

- 强制删除未跟踪的文件：

`git clean {{[-f|--force]}}`

- 强制删除未跟踪的目录：

`git clean {{[-f|--force]}} -d`

- 删除未跟踪的文件（包括被忽略的文件，在 `.gitignore` 和 `.git/info/exclude`的文件）：

`git clean -x`
