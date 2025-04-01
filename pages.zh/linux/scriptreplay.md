# scriptreplay

> 重放由 `script` 命令创建的 typescript 到标准输出。
> 更多信息：<https://manned.org/scriptreplay>.

- 以记录的速度重放 typescript：

`scriptreplay {{path/to/timing_file}} {{path/to/typescript}}`

- 以两倍于原始速度重放 typescript：

`scriptreplay {{path/to/timingfile}} {{path/to/typescript}} 2`

- 以原始速度的二分之一重放 typescript：

`scriptreplay {{path/to/timingfile}} {{path/to/typescript}} 0.5`
