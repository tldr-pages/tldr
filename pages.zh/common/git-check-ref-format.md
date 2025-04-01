# git check-ref-format

> 检查引用名称是否可接受，如果不可接受则以非零状态退出。
> 更多信息：<https://git-scm.com/docs/git-check-ref-format>.

- 检查指定引用名称的格式：

`git check-ref-format {{refs/head/refname}}`

- 打印上次检出的分支名称：

`git check-ref-format --branch @{-1}`

- 标准化引用名称：

`git check-ref-format --normalize {{refs/head/refname}}`
