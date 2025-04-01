# xmake

> 基于 Lua 的跨平台 C & C++ 构建工具。
> 更多信息：<https://xmake.io/#/getting_started>.

- 创建一个包含 hello world 和 `xmake.lua` 的 Xmake C 项目：

`xmake create --language c -P {{project_name}}`

- 构建并运行 Xmake 项目：

`xmake build run`

- 直接运行已编译的 Xmake 目标：

`xmake run {{target_name}}`

- 配置项目的构建目标：

`xmake config --plat={{macosx|linux|iphoneos|...}} --arch={{x86_64|i386|arm64|...}} --mode={{debug|release}}`

- 将编译的目标安装到目录中：

`xmake install -o {{path/to/directory}}`