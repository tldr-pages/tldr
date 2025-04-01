# dotenvx

> 一个更好的 `dotenv`，由 `dotenv` 的创建者打造。
> 更多信息：<https://dotenvx.com/docs>。

- 使用 `.env` 文件中的环境变量运行命令：

`dotenvx run -- {{command}}`

- 使用特定的 `.env` 文件中的环境变量运行命令：

`dotenvx run -f {{path/to/file.env}} -- {{command}}`

- 设置一个加密的环境变量：

`dotenvx set {{key}} {{value}}`

- 设置一个不加密的环境变量：

`dotenvx set {{key}} {{value}} --plain`

- 返回 `.env` 文件中定义的环境变量：

`dotenvx get`

- 返回 `.env` 文件中定义的特定环境变量的值：

`dotenvx get {{key}}`

- 返回 `.env` 文件和操作系统中的所有环境变量：

`dotenvx get --all`