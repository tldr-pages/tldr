# cmstp

> 管理连接服务配置文件。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>。

- 安装特定配置文件：

`cmstp "{{path\to\profile_file}}"`

- 安装时不创建桌面快捷方式：

`cmstp /ns "{{path\to\profile_file}}"`

- 安装时不检查依赖项：

`cmstp /nf "{{path\to\profile_file}}"`

- 仅为当前用户安装：

`cmstp /su "{{path\to\profile_file}}"`

- 为所有用户安装（需要管理员权限）：

`cmstp /au "{{path\to\profile_file}}"`

- 安装时静默进行，不显示任何提示：

`cmstp /s "{{path\to\profile_file}}"`

- 卸载特定配置文件：

`cmstp /u "{{path\to\profile_file}}"`

- 静默卸载，不显示确认提示：

`cmstp /u /s "{{path\to\profile_file}}"`