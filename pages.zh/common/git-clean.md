# git clean

> 从工作区中删除未被 Git 跟踪的文件。
> 更多信息：<https://git-scm.com/docs/git-clean>。

- 删除未被跟踪的文件：

`git clean`

- 交互式删除未被跟踪的文件：

`git clean {{[-i|--interactive]}}`

- 显示将要删除的文件，但不实际删除：

`git clean {{[-n|--dry-run]}}`

- 强制删除未被跟踪的文件：

`git clean {{[-f|--force]}}`

- 强制删除未被跟踪的目录：

`git clean {{[-f|--force]}} -d`

- 删除未被跟踪的文件，包括被排除的文件（在 `.gitignore` 和 `.git/info/exclude` 中忽略的文件）：

`git clean -x`
