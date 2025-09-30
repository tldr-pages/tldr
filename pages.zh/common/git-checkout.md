# git checkout

> 切换分支或将文件检出到工作区。
> 更多信息：<https://git-scm.com/docs/git-checkout>.

- 创建并切换到新分支：

`git checkout -b {{分支名}}`

- 基于指定引用（如分支、远程分支、标签等）创建并切换到新分支：

`git checkout -b {{分支名}} {{引用}}`

- 切换到已有的本地分支：

`git checkout {{分支名}}`

- 切换到上次检出的分支：

`git checkout -`

- 切换到已有的远程分支：

`git checkout {{[-t|--track]}} {{远程名}}/{{分支名}}`

- 丢弃当前目录下所有未暂存的更改（更多撤销操作见 `git reset`）：

`git checkout .`

- 丢弃对指定文件的未暂存更改：

`git checkout {{路径/到/文件}}`

- 用指定分支中提交的版本覆盖当前工作区的文件：

`git checkout {{分支名}} -- {{路径/到/文件}}`
