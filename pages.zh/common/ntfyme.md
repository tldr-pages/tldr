# ntfyme

> 一个通知工具，用于跟踪和通知您长时间运行的终止过程。
> 可通过 Gmail、Telegram 等发送成功/错误消息。
> 更多信息：<https://github.com/AnirudhG07/ntfyme>.

- 直接运行您的命令：

`ntfyme exec {{[-c|--cmd]}} {{command}}`

- 通过管道运行您的命令：

`echo {{command}} | ntfyme exec`

- 通过在引号中包含多个命令来运行它们：

`echo "{{command1; command2; command3}}" | ntfyme exec`

- 跟踪并在长时间挂起后终止进程：

`ntfyme exec {{[-t|--track-process]}} {{[-c|--cmd]}} {{command}}`

- 交互式设置工具配置：

`ntfyme setup`

- 加密您的密码：

`ntfyme enc`

- 查看日志历史：

`ntfyme log`

- 打开并编辑配置文件：

`ntfyme config`
