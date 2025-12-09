# git commit-tree

> 用于创建提交对象的底层工具。
> 参考： `git commit`.
> 更多信息：<https://git-scm.com/docs/git-commit-tree>.

- 创建带有指定提交信息的提交对象：

`git commit-tree {{树对象哈希}} -m "{{提交信息}}"`

- 从文件读取提交信息创建提交对象（使用 `-` 表示从标准输入读取）：

`git commit-tree {{树对象哈希}} -F {{路径/到/文件}}`

- 创建 GPG 签名过的提交对象：

`git commit-tree {{树对象哈希}} -m "{{提交信息}}" {{[-S|--gpg-sign]}}`

- 创建指定父提交的提交对象：

`git commit-tree {{树对象哈希}} -m "{{提交信息}}" -p {{父提交哈希}}`
