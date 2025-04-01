# doppler

> 使用 Doppler 管理不同环境中的环境变量。
> 某些子命令如 `run` 和 `secrets` 有其自身的使用文档。
> 更多信息：<https://docs.doppler.com/docs/cli>.

- 在当前目录中设置 Doppler CLI：

`doppler setup`

- 在当前目录中设置 Doppler 项目和配置：

`doppler setup`

- 使用秘密变量注入环境运行命令：

`doppler run --command {{command}}`

- 查看项目列表：

`doppler projects`

- 查看当前项目的秘密变量：

`doppler secrets`

- 在浏览器中打开 Doppler 仪表板：

`doppler open`