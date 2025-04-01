# bclm

> 在 MacBooks 上设置自定义充电限制。
> 更多信息：<https://github.com/zackelia/bclme>。

- 将充电限制设置为约 80%（对于 Intel 机器，电池充电水平可能会略低于设置值）：

`sudo bclm write {{77}}`

- 读取当前的充电限制：

`bclm read`

- 重启/SNC 重置后保持充电限制：

`sudo bclm persist`

- 移除持久化的充电限制：

`sudo bclm unpersist`
