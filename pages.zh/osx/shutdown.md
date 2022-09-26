# shutdown

> 关闭并重新启动系统。
> 更多信息：<https://ss64.com/osx/shutdown.html>.

- 立即关机：

`shutdown -h now`

- 立即休眠：

`shutdown -s now`

- 立即重启：

`shutdown -r now`

- 倒计时 5 分钟重启：

`shutdown -r +{{5}}`

- 在下午 1:00（使用 24 小时时钟）关机：

`shutdown -h {{1300}}`

- 在 2042 年 5 月 10 日上午 11:30 重新启动（输入格式：年年月月日日时时分分）：

`shutdown -r {{4205101130}}`
