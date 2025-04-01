# systemd-inhibit

> 禁止系统进入特定的电源状态。
> 抑制锁可以用于阻止或延迟系统睡眠和关机请求，以及自动处理空闲状态。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-inhibit.html>.

- 列出所有活动的抑制锁及其创建原因：

`systemd-inhibit --list`

- 使用 `sleep` 命令阻止系统关机指定的秒数：

`systemd-inhibit --what shutdown sleep {{5}}`

- 在下载完成前阻止系统进入睡眠或空闲状态：

`systemd-inhibit --what sleep:idle wget {{https://example.com/file}}`

- 在脚本退出前忽略盖子关闭开关：

`systemd-inhibit --what sleep:handle-lid-switch {{path/to/script}}`

- 在命令运行期间忽略电源按钮按下：

`systemd-inhibit --what handle-power-key {{command}}`

- 描述抑制器的创建者和原因（默认：命令及其参数用于 `--who` 和 `--why` 的“未知原因”）：

`systemd-inhibit --who {{$USER}} --why {{reason}} --what {{operation}} {{command}}`