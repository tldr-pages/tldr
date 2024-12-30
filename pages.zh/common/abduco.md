# abduco

> 终端会话管理器。
> 更多信息：<https://www.brain-dump.org/projects/abduco/>。

- 列出会话：

`abduco`

- [A] 附加到会话，如果会话不存在则创建它：

`abduco -A {{name}} {{bash}}`

- [A] 附加到会话并使用 `dvtm`，如果会话不存在则创建它：

`abduco -A {{name}}`

- 从会话中分离：

`<Ctrl> + \`

- [A] 以 [r] 只读模式附加到会话：

`abduco -Ar {{name}}`