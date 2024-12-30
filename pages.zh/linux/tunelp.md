# tunelp

> 设置并行端口设备的各种参数，以便故障排除或提高性能。
> 属于 `util-linux`。
> 更多信息：<https://manned.org/tunelp>。

- 检查并行端口设备的 [s]tatus：

`tunelp --status {{/dev/lp0}}`

- [r]eset 指定的并行端口：

`tunelp --reset {{/dev/lp0}}`

- 为设备使用给定的 [i]RQ，每个代表一个中断线：

`tunelp -i 5 {{/dev/lp0}}`

- 尝试指定的次数向打印机输出一个 [c]haracter，然后在指定的 [t]ime 内休眠：

`tunelp --chars {{times}} --time {{time_in_centiseconds}} {{/dev/lp0}}`

- 启用或禁用在错误时 [a]borting（默认禁用）：

`tunelp --abort {{on|off}}`