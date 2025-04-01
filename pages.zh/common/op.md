# op

> 1Password 桌面应用程序的官方命令行界面。
> 更多信息：<https://developer.1password.com/docs/cli/reference>.

- 登录 1Password 账户：

`op signin`

- 列出所有保险库：

`op vault list`

- 以 JSON 格式打印项目详情：

`op item get {{item_name}} --format json`

- 在默认保险库中创建一个新项目并指定类别：

`op item create --category {{category_name}}`

- 将引用的密钥打印到 `stdout`：

`op read {{secret_reference}}`

- 从导出的环境变量中传递密钥引用到命令：

`op run -- {{command}}`

- 从环境文件中传递密钥引用到命令：

`op run --env-file {{path/to/env_file.env}} -- {{command}}`

- 从文件中读取密钥引用并将明文密钥保存到文件中：

`op inject --in-file {{path/to/input_file}} --out-file {{path/to/output_file}}`
