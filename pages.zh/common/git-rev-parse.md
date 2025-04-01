# git rev-parse

> 显示与修订相关的元数据。
> 更多信息：<https://git-scm.com/docs/git-rev-parse>.

- 获取分支的提交哈希值：

`git rev-parse {{branch_name}}`

- 获取当前分支名称：

`git rev-parse --abbrev-ref {{HEAD}}`

- 获取根目录的绝对路径：

`git rev-parse --show-toplevel`
