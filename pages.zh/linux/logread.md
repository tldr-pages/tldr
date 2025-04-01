# logread

> 读取 `logd` 环形缓冲区日志。
> 更多信息：<https://openwrt.org/docs/guide-user/base-system/log.essentials>.

- 打印日志：

`logread`

- 打印 `n` 条消息：

`logread -l {{n}}`

- 通过（关键字/正则表达式）过滤消息：

`logread -e {{pattern}}`

- 实时打印日志消息：

`logread -f`

- 显示帮助：

`logread -h`