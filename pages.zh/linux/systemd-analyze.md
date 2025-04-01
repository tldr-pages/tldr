# systemd-analyze

> 分析和调试系统管理器。
> 显示系统启动过程中各个单元（服务、挂载点、设备、套接字）的时间详细信息。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-analyze.html>。

- 打印上次系统启动时间：

`systemd-analyze`

- 列出所有正在运行的单元，并按初始化时间排序：

`systemd-analyze blame`

- 打印时间关键链的单元树：

`systemd-analyze critical-chain`

- 创建一个 SVG 文件，显示每个系统服务启动的时间，并高亮显示它们的初始化时间：

`systemd-analyze plot > {{path/to/file.svg}}`

- 绘制依赖关系图并转换为 SVG 文件：

`systemd-analyze dot | dot -T {{svg}} > {{path/to/file.svg}}`

- 显示正在运行单元的安全评分：

`systemd-analyze security`