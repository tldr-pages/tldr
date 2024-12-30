# git commit-tree

> 低级实用工具，用于创建提交对象。
> 另见：`git commit`。
> 更多信息：<https://git-scm.com/docs/git-commit-tree>。

- 使用指定的消息创建提交对象：

`git commit-tree {{tree}} -m "{{message}}"`

- 从文件中读取消息以创建提交对象（使用 `-` 表示标准输入）：

`git commit-tree {{tree}} -F {{path/to/file}}`

- 创建一个 GPG 签名的提交对象：

`git commit-tree {{tree}} -m "{{message}}" --gpg-sign`

- 使用指定的父提交对象创建提交对象：

`git commit-tree {{tree}} -m "{{message}}" -p {{parent_commit_sha}}`