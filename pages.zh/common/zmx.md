# zmx

> 持久保留终端会话，使多个客户端能够附加。
> 另请参阅：`abduco`, `shpool`, `tmux`。
> 更多信息：<https://zmx.sh>。

- 创建指定名称的会话或附加到已有会话：

`zmx {{[a|attach]}} {{session_name}}`

- 列出活动会话：

`zmx {{[l|list|ls]}}`

- 从当前客户端分离（在 zmx 会话中）：

`<Ctrl \>`

- 无需附加即可在会话中执行非交互式命令：

`zmx {{[r|run]}} {{session_name}} {{command arguments...}}`

- 在会话中执行命令，并从调用终端分离：

`zmx {{[r|run]}} {{session_name}} -d {{command arguments...}}`

- 等待一个或多个会话中的任务完成：

`zmx {{[w|wait]}} {{session_name1 session_name2 ...}}`

- 终止指定名称的会话：

`zmx {{[k|kill]}} {{session_name}}`

- 显示会话回滚缓冲区的最后 100 行：

`zmx {{[hi|history]}} {{session_name}} | tail -100`
