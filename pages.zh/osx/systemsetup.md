# 系统设置

> 配置系统偏好设置的机器设置。
> 更多信息：<https://support.apple.com/guide/remote-desktop/about-systemsetup-apd95406b8d/mac>。

- 启用远程登录（SSH）：

`systemsetup -setremotelogin on`

- 指定时区、NTP 服务器并启用网络时间：

`systemsetup -settimezone "{{US/Pacific}}" -setnetworktimeserver {{us.pool.ntp.org}} -setusingnetworktime on`

- 让机器永不进入睡眠状态，并在断电或内核恐慌时自动重启：

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- 列出有效的启动磁盘：

`systemsetup -liststartupdisks`

- 指定一个新的启动磁盘：

`systemsetup -setstartupdisk {{path/to/directory}}`