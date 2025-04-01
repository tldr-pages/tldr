# physlock

> 锁定所有控制台和虚拟终端。
> 更多信息：<https://github.com/muennich/physlock>.

- 锁定所有控制台（需要当前用户或root解锁）：

`physlock`

- 锁定时在控制台上静音内核消息：

`physlock -m`

- 锁定时禁用 SysRq 机制：

`physlock -s`

- 在密码提示之前显示消息：

`physlock -p "{{已锁定！}}"`

- 分离并释放 physlock（适用于挂起或休眠脚本）：

`physlock -d`
