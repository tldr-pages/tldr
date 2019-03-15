# systemsetup

> 配置系统首选项计算机设置.

- 启用远程登录(SSH):

`systemsetup -setremotelogin on`

- 指定时区、NTP服务器并启用网络时间:

`systemsetup -settimezone {{美国/太平洋}} -setnetworktimeserver {{us.pool.ntp.org}} -setusingnetworktime on`

- 使机器从不休眠,并在电源故障或内核死机时自动重新启动:

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- disks 选择启动:

`systemsetup -liststartupdisks`

- 指定新的启动盘:

`systemsetup -setstartupdisk {{路径}}`
