# tuckr

> 用Rust编写的dotfile管理器。
> 另请参见：`chezmoi`，`vcsh`，`homeshick`，`stow`。
> 更多信息：<https://github.com/RaphGL/Tuckr>。

- 检查dotfile状态：

`tuckr status`

- 将所有dotfile添加到系统：

`tuckr add \*`

- 添加所有dotfile，除了指定的程序：

`tuckr add \* -e {{program1}},{{program2}}`

- 从系统中移除所有dotfile：

`tuckr rm \*`

- 添加程序的dotfile并运行其设置脚本：

`tuckr set {{program}}`