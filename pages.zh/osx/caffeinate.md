# caffeinate

> 防止 Mac 进入休眠模式。
> 更多信息：<https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- 防止进入休眠模式 , 1 小时内（3600 秒）：

`caffeinate -u -t {{3600}}`

- 在指定命令执行完前，禁止进入休眠：

`caffeinate -s {{命令}}`

- 在你按 Ctrl-C 之前禁止进入休眠模式：

`caffeinate -i`
