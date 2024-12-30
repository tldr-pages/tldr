# Ninja

> 一个旨在快速的构建系统。
> 更多信息：<https://ninja-build.org/manual.html>。

- 在当前目录中构建：

`ninja`

- 在当前目录中构建，同时并行执行 4 个任务：

`ninja -j {{4}}`

- 在指定目录中构建程序：

`ninja -C {{path/to/directory}}`

- 显示目标（例如 `install` 和 `uninstall`）：

`ninja -t targets`

- 显示帮助信息：

`ninja -h`