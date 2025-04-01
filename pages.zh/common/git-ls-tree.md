# git ls-tree

> 列出树对象的内容。
> 更多信息：<https://git-scm.com/docs/git-ls-tree>。

- 列出分支上树的内容：

`git ls-tree {{branch_name}}`

- 列出提交上树的内容，并递归到子树：

`git ls-tree -r {{commit_hash}}`

- 仅列出提交上树的文件名：

`git ls-tree --name-only {{commit_hash}}`

- 以树形结构打印当前分支 HEAD 的文件名（注意：Windows 上不支持 `tree --fromfile`）：

`git ls-tree -r --name-only HEAD | tree --fromfile`