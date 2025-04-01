# git mktree

> 使用 `ls-tree` 格式的文本构建树对象。
> 更多信息：<https://git-scm.com/docs/git-mktree>。

- 构建树对象并验证每个树条目的哈希标识一个已存在的对象：

`git mktree`

- 允许缺少的对象：

`git mktree --missing`

- 读取树对象的 NUL ([z]ero character) 分隔的输出（`ls-tree -z`）：

`git mktree -z`

- 允许创建多个树对象：

`git mktree --batch`

- 从 `stdin` 排序并构建树（需要非递归的 `git ls-tree` 输出格式）：

`git mktree < {{path/to/tree.txt}}`
