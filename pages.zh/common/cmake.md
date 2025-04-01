# cmake

> 跨平台构建自动化系统，用于生成本机构建系统的配方。
> 更多信息：<https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- 使用项目目录中的 `CMakeLists.txt` 在当前目录生成构建配方：

`cmake {{path/to/project_directory}}`

- 使用 CMake 变量将构建类型设置为 `Release` 并生成构建配方：

`cmake {{path/to/project_directory}} -D {{CMAKE_BUILD_TYPE=Release}}`

- 使用指定的构建系统 `generator_name` 生成构建配方：

`cmake -G {{generator_name}} {{path/to/project_directory}}`

- 使用指定目录中的生成的配方构建工件：

`cmake --build {{path/to/build_directory}}`

- 将构建工件安装到 `/usr/local/` 并去除调试符号：

`cmake --install {{path/to/build_directory}} --strip`

- 使用自定义路径前缀安装构建工件：

`cmake --install {{path/to/build_directory}} --strip --prefix {{path/to/directory}}`

- 运行自定义构建目标：

`cmake --build {{path/to/build_directory}} --target {{target_name}}`

- 显示帮助，获取生成器列表：

`cmake --help`
