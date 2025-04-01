# rfkill

> 启用和禁用无线设备。
> 更多信息：<https://manned.org/rfkill>.

- 列出设备：

`rfkill`

- 按列过滤：

`rfkill {{[-o|--output]}} {{ID,TYPE,DEVICE}}`

- 按类型（例如：bluetooth, wlan）禁用设备：

`rfkill block {{bluetooth}}`

- 按类型（例如：bluetooth, wlan）启用设备：

`rfkill unblock {{wlan}}`

- 以 JSON 格式输出：

`rfkill {{[-J|--json]}}`
