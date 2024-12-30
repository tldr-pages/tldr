# 鱼

> 友好的交互式 shell（Friendly Interactive SHell），一种旨在用户友好的命令行解释器。
> 更多信息：<https://fishshell.com>。

- 启动交互式 shell 会话：

`fish`

- 启动不加载启动配置的交互式 shell 会话：

`fish --no-config`

- 执行特定命令：

`fish --command "{{echo 'fish is executed'}}"`

- 执行特定脚本：

`fish {{path/to/script.fish}}`

- 检查特定脚本的语法错误：

`fish --no-execute {{path/to/script.fish}}`

- 从 `stdin` 执行特定命令：

`{{echo "echo 'fish is executed'"}} | fish`

- 以私密模式启动交互式 shell 会话，此模式下 shell 不会访问旧历史记录或保存新历史记录：

`fish --private`

- 定义并导出一个跨 shell 重启的环境变量（内置）：

`set --universal --export {{variable_name}} {{variable_value}}`