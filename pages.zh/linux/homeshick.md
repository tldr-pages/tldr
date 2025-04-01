# homeshick

> 同步 Git 配置文件。
> 参见: `chezmoi`, `stow`, `tuckr`, `vcsh`。
> 更多信息: <https://github.com/andsens/homeshick/wiki>。

- 创建一个新仓库:

`homeshick generate {{castle_name}}`

- 将文件添加到仓库:

`homeshick track {{castle_name}} {{path/to/file}}`

- 进入仓库:

`homeshick cd {{castle_name}}`

- 克隆仓库:

`homeshick clone {{github_username}}/{{repository_name}}`

- 为仓库中的所有文件创建符号链接:

`homeshick link {{castle_name}}`