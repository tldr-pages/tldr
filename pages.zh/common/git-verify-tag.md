# git verify-tag

> 检查标签的 GPG 签名。
> 如果标签没有签名，将出现错误。
> 更多信息：<https://git-scm.com/docs/git-verify-tag>.

- 检查标签是否有 GPG 签名：

`git verify-tag {{tag1 可选_tag2 ...}}`

- 检查标签是否有 GPG 签名并显示每个标签的详细信息：

`git verify-tag {{tag1 可选_tag2 ...}} --verbose`

- 检查标签是否有 GPG 签名并打印原始详细信息：

`git verify-tag {{tag1 可选_tag2 ...}} --raw`
