# pio ci

> 构建任意源代码结构的 PlatformIO 项目。
> 这将创建一个临时项目，将源代码复制到其中。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html>。

- 在默认的系统临时目录中构建 PlatformIO 项目并在构建后删除：

`pio ci {{path/to/project}}`

- 构建 PlatformIO 项目并指定特定的库：

`pio ci --lib {{path/to/library_directory}} {{path/to/project}}`

- 构建 PlatformIO 项目并指定特定的开发板（`pio boards` 列出所有开发板）：

`pio ci --board {{board}} {{path/to/project}}`

- 在特定目录中构建 PlatformIO 项目：

`pio ci --build-dir {{path/to/build_directory}} {{path/to/project}}`

- 构建 PlatformIO 项目并保留构建目录：

`pio ci --keep-build-dir {{path/to/project}}`

- 使用特定的配置文件构建 PlatformIO 项目：

`pio ci --project-conf {{path/to/platformio.ini}}`
