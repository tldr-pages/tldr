# stow

> 符号链接管理器。
> 常用于管理点文件（dotfiles）。
> 其他相关工具：`chezmoi`、`tuckr`、`vcsh`、`homeshick`。
> 更多信息：<https://www.gnu.org/software/stow/manual/html_node/Invoking-Stow.html>。

- 递归地将所有文件符号链接到指定目录：

`stow {{[-t|--target]}} {{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- 从指定目录递归地删除符号链接：

`stow {{[-D|--delete]}} {{[-t|--target]}} {{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- 模拟操作以查看结果：

`stow {{[-n|--simulate]}} {{[-t|--target]}} {{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- 删除并重新符号链接：

`stow {{[-R|--restow]}} {{[-t|--target]}} {{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- 排除匹配正则表达式的文件：

`stow --ignore={{regular_expression}} {{[-t|--target]}} {{path/to/target_directory}} {{file1 directory1 file2 directory2}}`