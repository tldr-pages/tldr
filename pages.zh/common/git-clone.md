# git clone

> 克隆现有的代码库。
> 更多信息：<https://git-scm.com/docs/git-clone>.

- 克隆一个现有的代码库：

`git clone {{远程代码库地址}}`

- 克隆一个现有的代码库到指定文件夹：

`git clone {{远程代码库地址}} {{路径/到/文件夹}}`

- 克隆一个现有的代码库和它的子模块：

`git clone --recursive {{远程代码库地址}}`

- 克隆一个本地的代码库：

`git clone -l {{路径/到/本地/代码库名}}`

- 静默克隆，不打印任何日志：

`git clone -q {{远程代码库地址}}`

- 克隆一个现有的代码库，只获取默认分支上10个最新的提交（对节省时间很有用）：

`git clone --depth {{10}} {{远程代码库地址}}`

- 克隆一个现有的、特定远程分支的代码库：

`git clone --branch {{分支名称}} --single-branch {{远程代码库地址}}`

- 使用 SSH 命令克隆一个现有的代码库：

`git clone --config core.sshCommand="{{ssh -i 路径/到/ssh_私钥}}" {{远程代码库地址}}`
