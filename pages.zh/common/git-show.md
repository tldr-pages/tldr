# git show

> 显示各种类型的 Git 对象（提交、标签等）。
> 更多信息：<https://git-scm.com/docs/git-show>。

- 显示最新提交的信息（哈希值、提交信息、更改及其他元数据）：

`git show`

- 显示指定提交的信息：

`git show {{commit}}`

- 显示与指定标签关联的提交的信息：

`git show {{tag}}`

- 显示分支头部第 3 个提交的信息：

`git show {{branch}}~{{3}}`

- 以单行显示提交信息，不显示差异输出：

`git show --oneline -s {{commit}}`

- 仅显示更改文件的统计信息（添加/删除的字符）：

`git show --stat {{commit}}`

- 仅显示添加、重命名或删除的文件列表：

`git show --summary {{commit}}`

- 显示指定修订版本（如分支、标签或提交）时文件的内容：

`git show {{revision}}:{{path/to/file}}`