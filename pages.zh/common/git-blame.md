# git blame

> 显示文件每行的提交哈希和最后作者。
> 更多信息：<https://git-scm.com/docs/git-blame>。

- 打印文件，每行显示作者名和提交哈希：

`git blame {{path/to/file}}`

- 打印文件，每行显示作者邮箱和提交哈希：

`git blame {{-e|--show-email}} {{path/to/file}}`

- 在特定提交下打印文件，每行显示作者名和提交哈希：

`git blame {{commit}} {{path/to/file}}`

- 在特定提交之前打印文件，每行显示作者名和提交哈希：

`git blame {{commit}}~ {{path/to/file}}`