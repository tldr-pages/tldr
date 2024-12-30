# bclm

> 在MacBook上设置自定义充电限制。
> 更多信息：<https://github.com/zackelia/bclme>。

- 将充电限制设置为约80%（对于Intel机器，电池充电水平可能会略低于设定值）：

`sudo bclm write {{77}}`

- 读取当前充电限制：

`bclm read`

- 在重启/SMC重置后保持充电限制：

`sudo bclm persist`

- 移除持久充电限制：

`sudo bclm unpersist`