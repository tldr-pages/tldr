# git check-ref-format

> 检查引用名称格式是否合法，不合法时返回非零状态码。
> 更多信息：<https://git-scm.com/docs/git-check-ref-format>.

- 检查指定引用名称的格式是否合法：

`git check-ref-format {{refs/head/refname}}`

- 打印最近检出的分支名称

`git check-ref-format --branch @{-1}`

- 规范化引用名称格式：

`git check-ref-format --normalize {{refs/head/refname}}`
