# konsave

> 使用一个命令保存和应用您的 Linux 自定义设置。
> 更多信息：<https://github.com/Prayag2/konsave>.

- 保存当前配置为一个配置文件：

`konsave --save {{profile_name}}`

- 应用一个配置文件：

`konsave --apply {{profile_name}}`

- 保存当前配置为一个配置文件，如果存在同名的配置文件则覆盖：

`konsave -s {{profile_name}} --force`

- 列出所有配置文件：

`konsave --list`

- 删除一个配置文件：

`konsave --remove {{profile_name}}`

- 导出一个配置文件为 `.knsv` 文件到主目录：

`konsave --export-profile {{profile_name}}`

- 导入一个 `.knsv` 配置文件：

`konsave --import-profile {{path/to/profile_name.knsv}}`
