# ninja

> 一个快速的构建系统。
> 更多信息：<https://ninja-build.org/manual.html>.

- 在当前目录下构建：

`ninja`

- 在当前目录下构建，最多并行执行 4 个作业：

`ninja -j {{4}}`

- 在指定的目录中构建一个程序：

`ninja -C {{路径}}`

- 查看 target（如 `install` 和 `uninstall`）：

`ninja -t targets`

- 查看帮助：

`ninja -h`
