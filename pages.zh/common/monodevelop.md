# MonoDevelop

> 跨平台的C#、F#等语言的集成开发环境（IDE）。
> 更多信息：<https://www.monodevelop.com/>。

- 启动MonoDevelop：

`monodevelop`

- 打开特定文件：

`monodevelop {{path/to/file}}`

- 在特定位置打开特定文件：

`monodevelop {{path/to/file}};{{line_number}};{{column_number}}`

- 强制在新窗口中打开，而不是切换到现有窗口：

`monodevelop --new-window`

- 禁用将`stdout`和`stderr`重定向到日志文件：

`monodevelop --no-redirect`

- 启用性能监控：

`monodevelop --perf-log`