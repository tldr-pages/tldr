# calcurse

> 一款基于文本的日历和调度应用程序，适用于命令行。
> 更多信息：<https://calcurse.org>。

- 在交互模式下启动 `calcurse`：

`calcurse`

- 打印当前日期的约会和事件并退出：

`calcurse --appointment`

- 移除所有本地 calcurse 项目并导入远程对象：

`calcurse-caldav --init=keep-remote`

- 移除所有远程对象并推送本地 calcurse 项目：

`calcurse-caldav --init=keep-local`

- 将本地对象复制到 CalDAV 服务器，反之亦然：

`calcurse-caldav --init=two-way`