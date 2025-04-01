# git blame

> 显示文件每一行的提交哈希和最后的作者。
> 更多信息：<https://git-scm.com/docs/git-blame>。

- 打印文件，每行显示作者名称和提交哈希：

`git blame {{path/to/file}}`

- 打印文件，每行显示作者邮箱和提交哈希：

`git blame {{[-e|--show-email]}} {{path/to/file}}`

- 在特定提交时打印文件，每行显示作者名称和提交哈希：

`git blame {{commit}} {{path/to/file}}`

- 在特定提交之前的版本打印文件，每行显示作者名称和提交哈希：

`git blame {{commit}}~ {{path/to/file}}`

- 打印特定行范围的作者名称和提交哈希信息：

`git blame -L {{start_line}},{{end_line}} {{path/to/file}}`

- 忽略空白和行移动：

`git blame -w -C -C -C {{path/to/file}}`