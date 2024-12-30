# cmake

> 跨平台构建自动化系统，生成本地构建系统的构建配方。
> 更多信息： <https://cmake.org/cmake/help/latest/manual/cmake.1.html>。

- 从项目目录生成当前目录中带有 `CMakeLists.txt` 的构建配方：

`cmake {{path/to/project_directory}}`

- 设置构建类型为 `Release` 的构建配方，使用 CMake 变量：

`cmake {{path/to/project_directory}} -D {{CMAKE_BUILD_TYPE=Release}}`

- 使用 `generator_name` 作为底层构建系统生成构建配方：

`cmake -G {{generator_name}} {{path/to/project_directory}}`

- 使用给定目录中生成的配方构建工件：

`cmake --build {{path/to/build_directory}}`

- 将构建工件安装到 `/usr/local/` 并去除调试符号：

`cmake --install {{path/to/build_directory}} --strip`

- 使用自定义前缀安装构建工件的路径：

`cmake --install {{path/to/build_directory}} --strip --prefix {{path/to/directory}}`

- 运行自定义构建目标：

`cmake --build {{path/to/build_directory}} --target {{target_name}}`

- 显示帮助，获取生成器列表：

`cmake --help`