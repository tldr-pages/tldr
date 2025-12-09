# ya

> 管理 Yazi 软件包和插件。
> 更多信息：<https://yazi-rs.github.io/docs/cli>.

- 添加一个软件包：

`ya pack -a {{软件包}}`

- 升级所有软件包：

`ya pack -u`

- 订阅来自所有远程实例的消息：

`ya sub {{种类}}`

- 向当前实例发布一个字符串内容的消息：

`ya pub --str {{字符串消息}}`

- 向当前实例发布一个 JSON 内容的消息：

`ya pub --json {{json消息}}`

- 向指定实例发布一个字符串内容的消息：

`ya pub-to --str {{消息}} {{接收者}} {{种类}}`
