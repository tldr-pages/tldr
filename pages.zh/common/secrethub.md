# secrethub

> 保持配置文件中没有敏感信息。
> 更多信息：<https://github.com/secrethub/secrethub-cli>.

- 将敏感信息打印到 `stdout`：

`secrethub read {{path/to/secret}}`

- 生成随机值并将其作为新的或更新的敏感信息存储：

`secrethub generate {{path/to/secret}}`

- 从剪贴板存储值作为新的或更新的敏感信息：

`secrethub write --clip {{path/to/secret}}`

- 从 `stdin` 提供的值作为新的或更新的敏感信息存储：

`echo "{{secret_value}}" | secrethub write {{path/to/secret}}`

- 审计仓库或敏感信息：

`secrethub audit {{path/to/repo_or_secret}}`