# konsave

> 通过一个命令保存并应用您的Linux自定义设置。
> 更多信息：<https://github.com/Prayag2/konsave>。

- 将当前配置保存为一个配置文件：

`konsave --save {{profile_name}}`

- 应用一个配置文件：

`konsave --apply {{profile_name}}`

- 将当前配置保存为一个配置文件，如果存在同名的配置文件则覆盖：

`konsave -s {{profile_name}} --force`

- 列出所有配置文件：

`konsave --list`

- 删除一个配置文件：

`konsave --remove {{profile_name}}`

- 将配置文件导出为`.knsv`到主目录：

`konsave --export-profile {{profile_name}}`

- 导入一个`.knsv`配置文件：

`konsave --import-profile {{path/to/profile_name.knsv}}`