# tuckr

> 用 Rust 编写的点文件管理器。
> 参见：`chezmoi`，`vcsh`，`homeshick`，`stow`。
> 更多信息：<https://github.com/RaphGL/Tuckr>。

- 检查点文件状态：

`tuckr status`

- 将所有点文件添加到系统：

`tuckr add \*`

- 将所有点文件添加到系统，但排除指定的程序：

`tuckr add \* -e {{program1}},{{program2}}`

- 从系统中移除所有点文件：

`tuckr rm \*`

- 添加程序的点文件并运行其设置脚本：

`tuckr set {{program}}`
