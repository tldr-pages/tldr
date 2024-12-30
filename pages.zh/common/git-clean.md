# git clean

> 从工作树中移除未被 Git 跟踪的文件。
> 更多信息：<https://git-scm.com/docs/git-clean>。

- 删除未被跟踪的文件：

`git clean`

- 以交互方式删除未被跟踪的文件：

`git clean {{-i|--interactive}}`

- 显示将被删除的文件，但不实际删除它们：

`git clean --dry-run`

- 强制删除未被跟踪的文件：

`git clean {{-f|--force}}`

- 强制删除未被跟踪的[d]irectory（目录）：

`git clean {{-f|--force}} -d`

- 删除未被跟踪的文件，包括被排除的[e]xcluded 文件（在 `.gitignore` 和 `.git/info/exclude` 中被忽略的文件）：

`git clean -x`