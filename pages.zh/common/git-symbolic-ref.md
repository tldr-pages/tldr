# git symbolic-ref

> 读取、更改或删除存储引用的文件。
> 更多信息：<https://git-scm.com/docs/git-symbolic-ref>。

- 通过名称存储引用：

`git symbolic-ref refs/{{name}} {{ref}}`

- 通过名称存储引用，并附带更新原因的消息：

`git symbolic-ref -m "{{message}}" refs/{{name}} refs/heads/{{branch_name}}`

- 通过名称读取引用：

`git symbolic-ref refs/{{name}}`

- 通过名称删除引用：

`git symbolic-ref --delete refs/{{name}}`

- 用于脚本时，使用 `--quiet` 隐藏错误，并使用 `--short` 简化输出（例如 "refs/heads/X" 输出为 "X"）：

`git symbolic-ref --quiet --short refs/{{name}}`