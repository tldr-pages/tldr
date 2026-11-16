# cmake

> 跨平台构建自动化系统，可为原生构建系统生成构建文件。
> 更多信息：<https://cmake.org/cmake/help/latest/manual/cmake.1.html>。

- 在当前目录中，根据项目目录中的 `CMakeLists.txt` 生成构建文件：

`cmake {{路径/到/项目目录}}`

- 使用指定目录中已生成的构建文件来构建产物：

`cmake --build {{路径/到/构建目录}}`

- 将构建产物安装到 `/usr/local/` 并去除调试符号：

`cmake --install {{路径/到/构建目录}} --strip`

- 生成构建文件，并通过 CMake 变量将构建类型设置为 `Release`：

`cmake {{路径/到/项目目录}} -D CMAKE_BUILD_TYPE=Release`

- 使用指定的生成器为底层构建系统生成构建文件：

`cmake -G {{生成器名称}} {{路径/到/项目目录}}`

- 安装构建产物，并为安装路径指定自定义前缀：

`cmake --install {{路径/到/构建目录}} --strip --prefix {{路径/到/目录}}`

- 运行自定义的构建目标：

`cmake --build {{路径/到/构建目录}} {{[-t|--target]}} {{目标名称}}`

- 显示帮助：

`cmake {{[-h|--help]}}`
