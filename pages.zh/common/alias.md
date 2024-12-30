# 别名

> 创建别名 - 被命令字符串替换的词。
> 别名在当前 shell 会话中过期，除非在 shell 的配置文件中定义，例如 `~/.bashrc`。
> 更多信息：<https://tldp.org/LDP/abs/html/aliases.html>。

- 列出所有别名：

`alias`

- 创建一个通用别名：

`alias {{word}}="{{command}}"`

- 查看与给定别名关联的命令：

`alias {{word}}`

- 移除已别名的命令：

`unalias {{word}}`

- 将 `rm` 变为交互式命令：

`alias {{rm}}="{{rm --interactive}}"`

- 创建 `la` 作为 `ls --all` 的快捷方式：

`alias {{la}}="{{ls --all}}"`