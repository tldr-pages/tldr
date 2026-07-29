# cmake

> 跨平台构建自动化系统，用于生成本地构建系统的构建脚本。
> 更多信息：<https://cmake.org/cmake/help/latest/manual/cmake.1.html>。

- 根据项目目录中的 `CMakeLists.txt` 在当前目录生成构建脚本：

`cmake {{路径/到/项目目录}}`

- 使用指定目录中的构建脚本构建项目：

`cmake --build {{路径/到/构建目录}}`

- 将构建产物安装到 `/usr/local/` 并去除调试符号：

`cmake --install {{路径/到/构建目录}} --strip`

- 生成构建脚本并将构建类型设置为 `Release`：

`cmake {{路径/到/项目目录}} -D CMAKE_BUILD_TYPE=Release`

- 使用指定的生成器作为底层构建系统生成构建脚本：

`cmake -G {{生成器名称}} {{路径/到/项目目录}}`

- 使用自定义路径前缀安装构建产物：

`cmake --install {{路径/到/构建目录}} --strip --prefix {{路径/到/目录}}`

- 运行自定义构建目标：

`cmake --build {{路径/到/构建目录}} {{[-t|--target]}} {{目标名称}}`

- 显示帮助信息：

`cmake {{[-h|--help]}}`
