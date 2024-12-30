# stow

> 符号链接管理器。
> 常用于管理点文件（dotfiles）。
> 另请参见: `chezmoi`，`tuckr`，`vcsh`，`homeshick`。
> 更多信息: <https://www.gnu.org/software/stow>。

- 将所有文件递归符号链接到给定目录：

`stow --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- 从给定目录递归删除符号链接：

`stow --delete --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- 模拟以查看结果会是什么样子：

`stow --simulate --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- 删除并重新符号链接：

`stow --restow --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- 排除与正则表达式匹配的文件：

`stow --ignore={{regular_expression}} --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`