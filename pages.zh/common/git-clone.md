# git clone

> 克隆现有的代码仓库。
> 更多信息：<https://git-scm.com/docs/git-clone>.

- 克隆一个现有的代码仓库到指定目录：

`git clone {{远程代码库地址}} {{路径/到/目录}}`

- 克隆一个现有的代码库和它的子模块：

`git clone --recursive {{远程代码库地址}}`

- 仅克隆现有代码仓库的 `.git` 目录：

`git clone {{[-n|--no-checkout]}} {{远程_代码仓库_地址}}`

- 克隆一个本地的代码库：

`git clone {{[-l|--local]}} {{路径/到/本地/代码库名}}`

- 静默克隆，不打印任何日志：

`git clone {{[-q|--quiet]}} {{远程代码库地址}}`

- 克隆一个现有的代码库，只获取默认分支上10个最新的提交（对节省时间很有用）：

`git clone --depth 10 {{远程代码库地址}}`

- 克隆一个现有的、特定远程分支的代码库：

`git clone {{[-b|--branch]}} {{分支名称}} --single-branch {{远程代码库地址}}`

- 使用 SSH 命令克隆一个现有的代码库：

`git clone {{[-c|--config]}} core.sshCommand="{{ssh -i 路径/到/ssh_私钥}}" {{远程代码库地址}}`
