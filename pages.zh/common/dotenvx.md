# dotenvx

> 一个更好的 `dotenv`，由 `dotenv` 的创作者开发。
> 更多信息：<https://dotenvx.com/docs>。

- 使用来自 `.env` 文件的环境变量运行命令：

`dotenvx run -- {{command}}`

- 使用来自特定 `.env` 文件的环境变量运行命令：

`dotenvx run -f {{path/to/file.env}} -- {{command}}`

- 设置一个加密的环境变量：

`dotenvx set {{key}} {{value}}`

- 设置一个不加密的环境变量：

`dotenvx set {{key}} {{value}} --plain`

- 返回在 `.env` 文件中定义的环境变量：

`dotenvx get`

- 返回在 `.env` 文件中定义的环境变量的值：

`dotenvx get {{key}}`

- 返回来自 `.env` 文件和操作系统的所有环境变量：

`dotenvx get --all`