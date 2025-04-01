# pulumi config

> 管理 Pulumi 堆栈的配置。
> 更多信息：<https://www.pulumi.com/docs/iac/cli/commands/pulumi_config/>.

- 以 JSON 格式查看当前配置：

`pulumi config --json`

- 查看指定堆栈的配置：

`pulumi config --stack {{stack_name}}`

- 获取配置键的值：

`pulumi config get {{key}}`

- 删除配置值：

`pulumi config rm {{key}}`

- 从文件中为配置键设置值：

`cat {{path/to/file}} | pulumi config set {{key}}`

- 为配置键设置秘密值（例如 API 密钥）并以密文形式存储/显示：

`pulumi config set --secret {{key}} {{S3cr37_value}}`

- 从指定的配置文件中删除多个配置值：

`pulumi config --config-file {{path/to/file}} rm-all {{key1 key2 ...}}`
