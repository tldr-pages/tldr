# pio run

> 运行 PlatformIO 项目目标。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>。

- 列出所有可用的项目目标：

`pio run --list-targets`

- 列出特定环境下的所有可用项目目标：

`pio run --list-targets --environment {{environment}}`

- 运行所有目标：

`pio run`

- 运行指定环境的所有目标：

`pio run --environment {{environment1}} --environment {{environment2}}`

- 运行指定的目标：

`pio run --target {{target1}} --target {{target2}}`

- 运行指定配置文件的目标：

`pio run --project-conf {{path/to/platformio.ini}}`
