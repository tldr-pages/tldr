# systemd-inhibit

> 禁止系统进入某些电源状态。
> 抑制锁可用于阻止或延迟系统睡眠和关机请求以及自动空闲处理。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-inhibit.html>。

- 列出所有活动的抑制锁及其创建原因：

`systemd-inhibit --list`

- 使用 `sleep` 命令阻止系统关机指定的秒数：

`systemd-inhibit --what shutdown sleep {{5}}`

- 在下载完成之前，防止系统进入睡眠或空闲状态：

`systemd-inhibit --what sleep:idle wget {{https://example.com/file}}`

- 在脚本退出之前，忽略合盖开关：

`systemd-inhibit --what sleep:handle-lid-switch {{path/to/script}}`

- 在命令运行期间，忽略电源按钮按下：

`systemd-inhibit --what handle-power-key {{command}}`

- 描述谁以及为什么创建了抑制器（默认：命令及其参数作为 `--who`，`--why` 为 `Unknown reason`）：

`systemd-inhibit --who {{$USER}} --why {{reason}} --what {{operation}} {{command}}`