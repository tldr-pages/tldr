# cgclassify

> 将正在运行的任务移动到 `cgroups`。
> 更多信息：<https://manned.org/cgclassify>。

- 将具有特定 PID 的进程移动到 CPU 层次结构中的 student 控制组：

`cgclassify -g {{cpu:student}} {{1234}}`

- 根据 `/etc/cgrules.conf` 配置文件将具有特定 PID 的进程移动到控制组：

`cgclassify {{1234}}`

- 将具有特定 PID 的进程移动到 CPU 层次结构中的 student 控制组。注意：`cgred` 服务的守护进程不会更改特定 PID 及其子进程的 `cgroups`（基于 `/etc/cgrules.conf`）：

`cgclassify --sticky -g {{cpu:/student}} {{1234}}`
