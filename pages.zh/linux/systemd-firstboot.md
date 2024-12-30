# systemd-firstboot

> 在系统第一次启动时或之前初始化基本系统设置。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-firstboot.html>。

- 在指定目录上操作，而不是主机系统的根目录：

`sudo systemd-firstboot --root={{path/to/root_directory}}`

- 设置系统键盘布局：

`sudo systemd-firstboot --keymap={{keymap}}`

- 设置系统主机名：

`sudo systemd-firstboot --hostname={{hostname}}`

- 设置 root 用户的密码：

`sudo systemd-firstboot --root-password={{password}}`

- 交互式提示用户进行特定基本设置：

`sudo systemd-firstboot --prompt={{setting}}`

- 强制写入配置，即使相关文件已经存在：

`sudo systemd-firstboot --force`

- 移除所有由 `systemd-firstboot` 配置的现有文件：

`sudo systemd-firstboot --reset`

- 移除系统 root 用户的密码：

`sudo systemd-firstboot --delete-root-password`