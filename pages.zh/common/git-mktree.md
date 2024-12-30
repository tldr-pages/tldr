# git mktree

> 使用 `ls-tree` 格式化文本构建树对象。
> 更多信息请访问：<https://git-scm.com/docs/git-mktree>。

- 构建一个树对象，并验证每个树条目的哈希是否标识一个现有对象：

`git mktree`

- 允许缺失对象：

`git mktree --missing`

- 读取以 NUL（[z]ero 字符）终止的树对象输出（`ls-tree -z`）：

`git mktree -z`

- 允许创建多个树对象：

`git mktree --batch`

- 从 `stdin` 排序并构建树（需要非递归的 `git ls-tree` 输出格式）：

`git mktree < {{path/to/tree.txt}}`