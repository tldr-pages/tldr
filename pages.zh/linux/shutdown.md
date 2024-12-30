# 关机

> 关闭并重启系统。
> 更多信息：<https://manned.org/shutdown.8>。

- 立即关机（[h]alt）：

`shutdown -h now`

- 立即重启（[r]eboot）：

`shutdown -r now`

- 5分钟后重启（[r]eboot）：

`shutdown -r +{{5}} &`

- 在下午1:00关机（使用24小时制[h]钟）：

`shutdown -h 13:00`

- 取消待处理的关机/重启操作（[c]ancel）：

`shutdown -c`