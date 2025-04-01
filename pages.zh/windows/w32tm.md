# w32tm

> 查询和控制 w32time 时间同步服务。
> 更多信息：<https://learn.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings>.

- 显示当前时间同步状态：

`w32tm /query /status /verbose`

- 显示与时间服务器的时间偏移图：

`w32tm /stripchart /computer:{{time_server}}`

- 显示来自时间服务器的 NTP 回复：

`w32tm /stripchart /packetinfo /samples:1 /computer:{{time_server}}`

- 显示当前使用的时间服务器状态：

`w32tm /query /peers`

- 显示 w32time 服务的配置（在提升的命令提示符下运行）：

`w32tm /query /configuration`

- 立即强制时间重新同步（在提升的命令提示符下运行）：

`w32tm /resync /force`

- 将 w32time 调试日志写入文件（在提升的命令提示符下运行）：

`w32tm /debug /enable /file:{{path\to\debug.log}} /size:{{10000000}} /entries:{{0-300}}`