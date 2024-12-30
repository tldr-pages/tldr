# physlock

> 锁定所有控制台和虚拟终端。
> 更多信息：<https://github.com/muennich/physlock>。

- 锁定每个控制台（需要当前用户或root解锁）：

`physlock`

- 在锁定时静音控制台上的内核消息：

`physlock -m`

- 在锁定时禁用SysRq机制：

`physlock -s`

- 在密码提示之前显示一条消息：

`physlock -p "{{Locked!}}"`

- 生成并分离physlock（对挂起或休眠脚本很有用）：

`physlock -d`