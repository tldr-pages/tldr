# xmake

> 一个基于 Lua 的跨平台 C 和 C++ 构建工具。
> 更多信息：<https://xmake.io/#/getting_started>。

- 创建一个 Xmake C 项目，包含 Hello World 和 `xmake.lua` 文件：

`xmake create --language c -P {{project_name}}`

- 构建并运行一个 Xmake 项目：

`xmake build run`

- 直接运行一个已编译的 Xmake 目标：

`xmake run {{target_name}}`

- 配置项目的构建目标：

`xmake config --plat={{macosx|linux|iphoneos|...}} --arch={{x86_64|i386|arm64|...}} --mode={{debug|release}}`

- 将编译后的目标安装到指定目录：

`xmake install -o {{path/to/directory}}`