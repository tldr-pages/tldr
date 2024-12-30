# ya

> 管理 Yazi 包和插件。
> 更多信息：<https://github.com/sxyazi/yazi>。

- 添加一个包：

`ya pack -a {{package}}`

- 升级所有包：

`ya pack -u`

- 订阅来自所有远程实例的消息：

`ya sub {{kinds}}`

- 向当前实例发布字符串消息：

`ya pub --str {{string_message}}`

- 向当前实例发布 JSON 消息：

`ya pub --json {{json_message}}`

- 向指定实例发布字符串消息：

`ya pub-to --str {{message}} {{receiver}} {{kind}}`