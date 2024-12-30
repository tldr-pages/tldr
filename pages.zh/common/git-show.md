# git show

> 显示各种类型的 Git 对象（提交、标签等）。
> 更多信息：<https://git-scm.com/docs/git-show>。

- 显示最新提交的信息（哈希、消息、变化和其他元数据）：

`git show`

- 显示给定提交的信息：

`git show {{commit}}`

- 显示与给定标签相关的提交信息：

`git show {{tag}}`

- 显示某个分支上距离 HEAD 的第 3 次提交的信息：

`git show {{branch}}~{{3}}`

- 以单行形式显示提交消息，抑制 diff 输出：

`git show --oneline -s {{commit}}`

- 仅显示更改文件的统计信息（添加/删除的字符）：

`git show --stat {{commit}}`

- 仅显示添加、重命名或删除的文件列表：

`git show --summary {{commit}}`

- 显示给定修订版（例如分支、标签或提交）时文件的内容：

`git show {{revision}}:{{path/to/file}}`