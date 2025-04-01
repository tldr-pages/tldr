# pio debug

> 调试 PlatformIO 项目。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>。

- 调试当前目录中的 PlatformIO 项目：

`pio debug`

- 调试指定的 PlatformIO 项目：

`pio debug --project-dir {{path/to/platformio_project}}`

- 调试特定的环境：

`pio debug --environment {{environment}}`

- 使用特定的配置文件调试 PlatformIO 项目：

`pio debug --project-conf {{path/to/platformio.ini}}`

- 使用 `gdb` 调试器调试 PlatformIO 项目：

`pio debug --interface={{gdb}} {{gdb_options}}`