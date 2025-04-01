# git commit-tree

> 用于创建提交对象的低级工具。
> 参见: `git commit`。
> 更多信息: <https://git-scm.com/docs/git-commit-tree>。

- 使用指定的消息创建提交对象：

`git commit-tree {{tree}} -m "{{message}}"`

- 从文件中读取消息创建提交对象（使用 `-` 表示从标准输入读取）：

`git commit-tree {{tree}} -F {{path/to/file}}`

- 创建带有 GPG 签名的提交对象：

`git commit-tree {{tree}} -m "{{message}}" --gpg-sign`

- 创建带有指定父提交对象的提交对象：

`git commit-tree {{tree}} -m "{{message}}" -p {{parent_commit_sha}}`
