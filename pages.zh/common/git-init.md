# git init

> 初始化新的本地 Git 仓库。
> 更多信息：<https://git-scm.com/docs/git-init>.

- 初始化新的本地仓库：

`git init`

- 初始化仓库，并指定初始分支的名字（通常默认为 `master` 或 `main`）：

`git init {{[-b|--initial-branch]}} {{分支名}}`

- 初始化仓库，使用 SHA256 算法生成对象哈希（需 Git 2.29+ 版本支持）：

`git init --object-format sha256`

- 创建裸仓库，适合用作 SSH 远程仓库：

`git init --bare`
