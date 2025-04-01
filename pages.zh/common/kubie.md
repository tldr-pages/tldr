# kubie

> 用于在 `kubectl` 上下文和命名空间之间切换的工具。
> 更多信息：<https://github.com/sbstp/kubie>。

- 显示可选择的上下文菜单：

`kubie ctx`

- 切换当前 shell 到指定的上下文：

`kubie ctx {{context}}`

- 切换当前 shell 到指定的命名空间：

`kubie ns {{namespace}}`

- 切换当前 shell 到指定的上下文和命名空间：

`kubie ctx {{context}} -n {{namespace}}`

- 在指定的上下文和命名空间中执行命令，不启动 shell：

`kubie exec {{context}} {{namespace}} {{command}}`

- 检查 Kubernetes 配置文件中的问题：

`kubie lint`
