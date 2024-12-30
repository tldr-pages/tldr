# homeshick

> 同步 Git dotfiles。
> 另见：`chezmoi`、`stow`、`tuckr`、`vcsh`。
> 更多信息：<https://github.com/andsens/homeshick/wiki>。

- 创建一个新城堡：

`homeshick generate {{castle_name}}`

- 向你的城堡添加一个文件：

`homeshick track {{castle_name}} {{path/to/file}}`

- 进入一个城堡：

`homeshick cd {{castle_name}}`

- 克隆一个城堡：

`homeshick clone {{github_username}}/{{repository_name}}`

- 从一个城堡中创建所有文件的符号链接：

`homeshick link {{castle_name}}`