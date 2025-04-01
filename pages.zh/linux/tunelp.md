# tunelp

> 为并行端口设备设置各种参数，以便故障排除或提高性能。
> 属于 `util-linux` 工具集。
> 更多信息：<https://manned.org/tunelp>.

- 检查并行端口设备的状态：

`tunelp {{[-s|--status]}} {{/dev/lp0}}`

- 重置指定的并行端口：

`tunelp {{[-r|--reset]}} {{/dev/lp0}}`

- 为设备使用指定的 IRQ，每个 IRQ 代表一个中断线：

`tunelp {{[-i|--irq]}} 5 {{/dev/lp0}}`

- 尝试在指定时间内向打印机输出字符的次数，如果失败则休眠一段时间：

`tunelp {{[-c|--chars]}} {{times}} {{[-t|--time]}} {{time_in_centiseconds}} {{/dev/lp0}}`

- 启用或禁用在错误时中止（默认禁用）：

`tunelp {{[-a|--abort]}} {{on|off}}`
