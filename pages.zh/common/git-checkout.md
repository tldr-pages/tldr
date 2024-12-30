# git checkout

> 检出一个分支或路径到工作树。
> 更多信息：<https://git-scm.com/docs/git-checkout>。

- 创建并切换到一个新分支：

`git checkout -b {{branch_name}}`

- 创建并切换到一个基于特定引用（例如分支、远程/分支、标签等有效引用）的新分支：

`git checkout -b {{branch_name}} {{reference}}`

- 切换到一个现有的本地分支：

`git checkout {{branch_name}}`

- 切换到上一个检出的分支：

`git checkout -`

- 切换到一个现有的远程分支：

`git checkout --track {{remote_name}}/{{branch_name}}`

- 丢弃当前目录中所有未暂存的更改（有关更多撤销类命令，请参见 `git reset`）：

`git checkout .`

- 丢弃特定文件的未暂存更改：

`git checkout {{path/to/file}}`

- 用给定分支中提交的版本替换当前目录中的文件：

`git checkout {{branch_name}} -- {{path/to/file}}`