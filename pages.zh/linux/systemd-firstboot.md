# systemd-firstboot

> 在系统首次启动或之前初始化基本系统设置。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-firstboot.html>.

- 操作指定目录而不是主机系统的根目录：

`sudo systemd-firstboot --root={{path/to/root_directory}}`

- 设置系统键盘布局：

`sudo systemd-firstboot --keymap={{keymap}}`

- 设置系统主机名：

`sudo systemd-firstboot --hostname={{hostname}}`

- 设置 root 用户的密码：

`sudo systemd-firstboot --root-password={{password}}`

- 交互式提示用户设置特定的基本配置：

`sudo systemd-firstboot --prompt={{setting}}`

- 即使相关文件已存在，也强制写入配置：

`sudo systemd-firstboot --force`

- 删除所有由 `systemd-firstboot` 配置的文件：

`sudo systemd-firstboot --reset`

- 删除系统的 root 用户的密码：

`sudo systemd-firstboot --delete-root-password`