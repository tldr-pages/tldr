# pio project

> 管理 PlatformIO 项目。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/project/>。

- 初始化一个新的 PlatformIO 项目：

`pio project init`

- 在指定目录中初始化一个新的 PlatformIO 项目：

`pio project init --project-dir {{path/to/project_directory}}`

- 初始化一个新的 PlatformIO 项目，指定板 ID：

`pio project init --board {{ATmega328P|uno|...}}`

- 初始化一个基于 PlatformIO 的项目，指定一个或多个项目选项：

`pio project init --project-option="{{option}}={{value}}" --project-option="{{option}}={{value}}"`

- 打印项目的配置：

`pio project config`
