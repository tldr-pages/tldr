# vcpkg

> C/C++ 库的包管理器。
> 注意：包不会安装到系统中。要使用它们，需要告诉你的构建系统（例如 CMake）使用 `vcpkg`。
> 更多信息：<https://learn.microsoft.com/en-us/vcpkg/>。

- 构建并添加 `libcurl` 到 `vcpkg` 环境：

`vcpkg install curl`

- 使用 `emscripten` 工具链构建并添加 `zlib`：

`vcpkg install --triplet=wasm32-emscripten zlib`

- 搜索包：

`vcpkg search {{pkg_name}}`

- 配置 CMake 项目以使用 `vcpkg` 包：

`cmake -B build -DCMAKE_TOOLCHAIN_FILE={{path/to/vcpkg_install_directory}}/scripts/buildsystems/vcpkg.cmake`
