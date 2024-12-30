# op

> 1Password桌面应用程序的官方CLI。
> 更多信息：<https://developer.1password.com/docs/cli/reference>。

- 登录到1Password帐户：

`op signin`

- 列出所有保险库：

`op vault list`

- 以JSON格式打印项目详细信息：

`op item get {{item_name}} --format json`

- 在默认保险库中创建一个新项目并指定类别：

`op item create --category {{category_name}}`

- 将引用的秘密打印到`stdout`：

`op read {{secret_reference}}`

- 将从导出的环境变量中获得的秘密引用传递给命令：

`op run -- {{command}}`

- 从环境文件中将秘密引用传递给命令：

`op run --env-file {{path/to/env_file.env}} -- {{command}}`

- 从文件中读取秘密引用并将明文秘密保存到文件中：

`op inject --in-file {{path/to/input_file}} --out-file {{path/to/output_file}}`