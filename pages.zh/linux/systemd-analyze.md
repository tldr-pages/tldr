# systemd-analyze

> 分析和调试系统管理器。
> 显示单位（服务、挂载点、设备、套接字）启动过程的时间细节。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-analyze.html>。

- 列出所有运行的单位，按初始化所需时间排序：

`systemd-analyze blame`

- 打印时间关键链的单位树：

`systemd-analyze critical-chain`

- 创建一个SVG文件，显示每个系统服务的启动时间，并突出显示它们在初始化上花费的时间：

`systemd-analyze plot > {{path/to/file.svg}}`

- 绘制依赖图并将其转换为SVG文件：

`systemd-analyze dot | dot -T{{svg}} > {{path/to/file.svg}}`

- 显示运行单位的安全评分：

`systemd-analyze security`