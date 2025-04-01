# git commit

> 将文件提交到仓库。
> 更多信息：<https://git-scm.com/docs/git-commit>.

- 将暂存的文件提交到仓库，附带提交说明信息：

`git commit {{[-m|--message]}} "{{信息}}"`

- 提交暂存的文件，并从指定文件中读取附带的提交信息：

`git commit {{[-F|--file]}} {{路径/到/提交信息文件}}`

- 自动暂存并提交所有修改过的和删除的文件，附带提交信息：

`git commit {{[-a|--all]}} {{[-m|--message]}} "{{信息}}"`

- 提交暂存的文件，并使用指定的 GPG 密钥签名（若未指定参数则使用配置文件中的设定）：

`git commit {{[-S|--gpg-sign]}} {{密钥ID}} {{[-m|--message]}} "{{信息}}"`

- 将当前暂存的更改追加到最近一次提交，并更新其哈希值：

`git commit --amend`

- 只提交指定的（已暂存的）文件：

`git commit {{路径/到/文件1 路径/到/文件2 ...}}`

- 即使没有暂存文件也创建提交：

`git commit {{[-m|--message]}} "{{信息}}" --allow-empty`
