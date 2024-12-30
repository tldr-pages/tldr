# secrethub

> 将秘密保存在配置文件之外。
> 更多信息：<https://github.com/secrethub/secrethub-cli>。

- 将秘密打印到 `stdout`：

`secrethub read {{path/to/secret}}`

- 生成随机值并将其作为新的或更新的秘密存储：

`secrethub generate {{path/to/secret}}`

- 将剪贴板中的值作为新的或更新的秘密存储：

`secrethub write --clip {{path/to/secret}}`

- 将从 `stdin` 提供的值作为新的或更新的秘密存储：

`echo "{{secret_value}}" | secrethub write {{path/to/secret}}`

- 审计一个仓库或秘密：

`secrethub audit {{path/to/repo_or_secret}}`