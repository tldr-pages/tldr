# git commit

> 将文件提交到版本库。
> 更多信息：<https://git-scm.com/docs/git-commit>。

- 将暂存文件提交到版本库并附上消息：

`git commit --message "{{message}}"`

- 从文件中读取消息并提交暂存文件：

`git commit --file {{path/to/commit_message_file}}`

- 自动暂存所有已修改和已删除的文件，并附上消息提交：

`git commit --all --message "{{message}}"`

- 提交暂存文件并使用指定的 GPG 密钥进行签名（如果未指定参数，则使用配置文件中定义的密钥）：

`git commit --gpg-sign {{key_id}} --message "{{message}}"`

- 通过添加当前暂存的更改更新上一个提交，更改提交的哈希值：

`git commit --amend`

- 仅提交特定（已经暂存）的文件：

`git commit {{path/to/file1 path/to/file2 ...}}`

- 创建一个提交，即使没有暂存文件：

`git commit --message "{{message}}" --allow-empty`