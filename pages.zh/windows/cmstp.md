# cmstp

> 用于管理连接服务配置文件的命令行工具。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- 安装指定的配置文件：

`cmstp "{{配置文件的路径}}"`

- 安装时不创建桌面快捷方式：

`cmstp /ns "{{配置文件的路径}}"`

- 安装时不检查依赖：

`cmstp /nf "{{配置文件的路径}}"`

- 仅为当前用户安装：

`cmstp /su "{{配置文件的路径}}"`

- 为所有用户安装（需要管理员权限）：

`cmstp /au "{{配置文件的路径}}"`

- 静默安装：

`cmstp /s "{{配置文件的路径}}"`

- 卸载一个指定的配置文件：

`cmstp /u "{{配置文件的路径}}"`

- 静默删除：

`cmstp /u /s "{{配置文件的路径}}"`
