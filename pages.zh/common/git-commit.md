# git commit

> 提交文件到仓库。
> 更多信息：<https://git-scm.com/docs/git-commit>.

- 将暂存文件提交到存储库并附带消息：

`git commit --message {{消息}}`

- 提交暂存文件并包含从文件中读取的消息：

`git commit --file {{路径/到/提交消息文件}}`

- 自动暂存所有修改过和被删除的文件并附带消息：

`git commit --all --message {{消息}}`

- 提交暂存文件并使用指定 GPG 密钥签名（如果没有参数指定则使用配置文件的参数）：

`git commit --gpg-sign {{密钥ID}} --message {{消息}}`

- 通过添加当前暂存的更改来更新最后一次提交，更改提交的哈希值：

`git commit --amend`

- 仅提交指定的（已经暂存的）文件：

`git commit {{路径/到/文件1}} {{路径/到/文件2}}`

- 创建提交，即使没有暂存文件：

`git commit --message "{{消息}}" --allow-empty`
