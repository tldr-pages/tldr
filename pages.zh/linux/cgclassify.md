# cgclassify

> 将正在运行的任务移动到 `cgroups`。
> 更多信息请访问：<https://manned.org/cgclassify>。

- 将具有特定 PID 的进程移动到 CPU 层次结构中的控制组 student：

`cgclassify -g {{cpu:student}} {{1234}}`

- 根据 `/etc/cgrules.conf` 配置文件将具有特定 PID 的进程移动到控制组：

`cgclassify {{1234}}`

- 将具有特定 PID 的进程移动到 CPU 层次结构中的控制组 student。注意：服务 `cgred` 的守护进程不会改变特定 PID 及其子进程的 `cgroups`（基于 `/etc/cgrules.conf`）：

`cgclassify --sticky -g {{cpu:/student}} {{1234}}`