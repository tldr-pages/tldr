# git verify-commit

> 检查提交的 GPG 签名。
> 如果没有提交被验证，则不会打印任何内容，无论指定的选项如何。
> 更多信息：<https://git-scm.com/docs/git-verify-commit>.

- 检查提交是否有 GPG 签名：

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}}`

- 检查提交是否有 GPG 签名并显示每个提交的详细信息：

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --verbose`

- 检查提交是否有 GPG 签名并打印原始详细信息：

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --raw`
