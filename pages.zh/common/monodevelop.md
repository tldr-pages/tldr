# monodevelop

> 跨平台的 C#、F# 等语言的集成开发环境 (IDE)。
> 更多信息：<https://www.monodevelop.com/>.

- 启动 MonoDevelop：

`monodevelop`

- 打开指定的文件：

`monodevelop {{path/to/file}}`

- 打开指定的文件，并将光标定位到指定位置：

`monodevelop {{path/to/file}};{{line_number}};{{column_number}}`

- 强制打开新窗口而不是切换到已有的窗口：

`monodevelop --new-window`

- 禁用将 `stdout` 和 `stderr` 重定向到日志文件：

`monodevelop --no-redirect`

- 开启性能监控：

`monodevelop --perf-log`
