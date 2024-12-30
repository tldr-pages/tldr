# git log

> 显示提交历史。
> 更多信息：<https://git-scm.com/docs/git-log>。

- 从当前提交开始，按逆时间顺序显示当前工作目录中 Git 仓库的提交序列：

`git log`

- 显示特定文件或目录的历史，包括差异：

`git log {{-p|-u|--patch}} {{path/to/file_or_directory}}`

- 显示每次提交中哪些文件发生了变化的概况：

`git log --stat`

- 使用每个提交信息的第一行显示当前分支的提交图：

`git log --oneline --graph`

- 显示整个仓库中所有提交、标签和分支的图：

`git log --oneline --decorate --all --graph`

- 仅显示包含特定字符串的提交信息，忽略大小写：

`git log {{-i|--regexp-ignore-case}} --grep {{search_string}}`

- 显示某位作者的最后 N 次提交：

`git log {{-n|--max-count}} {{number}} --author "{{author}}"`

- 显示两个日期之间的提交（yyyy-mm-dd）：

`git log --before "{{2017-01-29}}" --after "{{2017-01-17}}"`