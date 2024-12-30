# git init

> 初始化一个新的本地 Git 仓库。
> 更多信息：<https://git-scm.com/docs/git-init>。

- 初始化一个新的本地仓库：

`git init`

- 使用指定名称初始化初始分支的仓库：

`git init --initial-branch={{branch_name}}`

- 使用 SHA256 作为对象哈希初始化仓库（需要 Git 版本 2.29 及以上）：

`git init --object-format={{sha256}}`

- 初始化一个简化的仓库，适合用作 SSH 远程仓库：

`git init --bare`