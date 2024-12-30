# kubectx

> 管理和切换 `kubectl` 上下文的工具。
> 更多信息：<https://github.com/ahmetb/kubectx>。

- 列出上下文：

`kubectx`

- 切换到指定的上下文：

`kubectx {{name}}`

- 切换到上一个上下文：

`kubectx -`

- 重命名指定的上下文：

`kubectx {{alias}}={{name}}`

- 显示当前的上下文名称：

`kubectx -c`

- 删除指定的上下文：

`kubectx -d {{name}}`