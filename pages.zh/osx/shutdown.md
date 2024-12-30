# 关机

> 关闭并重启系统。
> 更多信息：<https://keith.github.io/xcode-man-pages/shutdown.8.html>。

- 立即关闭（停止）：

`shutdown -h now`

- 立即进入睡眠模式：

`shutdown -s now`

- 立即重启：

`shutdown -r now`

- 5分钟后重启：

`shutdown -r "+{{5}}"`

- 下午1:00关机（使用24小时制）：

`shutdown -h {{1300}}`

- 2042年5月10日下午11:30重启（输入格式：YYMMDDHHMM）：

`shutdown -r {{4205101130}}`