# git verify-tag

> 检查标签的 GPG 验证。
> 如果标签未签名，将会发生错误。
> 更多信息：<https://git-scm.com/docs/git-verify-tag>。

- 检查标签的 GPG 签名：

`git verify-tag {{tag1 optional_tag2 ...}}`

- 检查标签的 GPG 签名并显示每个标签的详细信息：

`git verify-tag {{tag1 optional_tag2 ...}} --verbose`

- 检查标签的 GPG 签名并打印原始详细信息：

`git verify-tag {{tag1 optional_tag2 ...}} --raw`