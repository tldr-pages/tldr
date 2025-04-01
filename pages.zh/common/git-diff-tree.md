# git diff-tree

> 比较通过两个树对象找到的 blob 的内容和模式。
> 更多信息：<https://git-scm.com/docs/git-diff-tree>。

- 比较两个树对象：

`git diff-tree {{tree-ish1}} {{tree-ish2}}`

- 显示两个特定提交之间的更改：

`git diff-tree -r {{commit1}} {{commit2}}`

- 以补丁格式显示更改：

`git diff-tree {{[-p|--patch]}} {{tree-ish1}} {{tree-ish2}}`

- 通过特定路径过滤更改：

`git diff-tree {{tree-ish1}} {{tree-ish2}} -- {{path/to/file_or_directory}}`