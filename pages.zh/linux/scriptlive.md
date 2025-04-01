# scriptlive

> 实时执行由 `script` 命令创建的 typescript。
> 参见：`script`。
> 更多信息：<https://manned.org/scriptlive>。

- 实时执行 typescript：

`scriptlive {{path/to/timing_file}} {{path/to/typescript}}`

- 以两倍于原始速度执行 typescript：

`scriptlive {{path/to/timing_file}} {{path/to/typescript}} --divisor 2`

- 执行使用 `script` 的 `--log-in` 选项创建的 typescript：

`scriptlive --log-in {{path/to/stdin_log_file}} {{path/to/typescript}}`

- 执行 typescript，每个命令之间最多等待 2 秒：

`scriptlive {{path/to/timing_file}} {{path/to/typescript}} --maxdelay 2`
