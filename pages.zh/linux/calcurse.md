# calcurse

> 基于文本的命令行日历和调度应用程序。
> 更多信息：<https://calcurse.org>。

- 以交互模式启动 `calcurse`：

`calcurse`

- 打印当天的约会和事件，然后退出：

`calcurse --appointment`

- 删除所有本地 calcurse 项目并导入远程对象：

`calcurse-caldav --init=keep-remote`

- 删除所有远程对象并推送本地 calcurse 项目：

`calcurse-caldav --init=keep-local`

- 将本地对象复制到 CalDAV 服务器，反之亦然：

`calcurse-caldav --init=two-way`
