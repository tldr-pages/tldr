# salt-call

> 在 Salt Minion 上本地调用 Salt。
> 更多信息：<https://docs.saltproject.io/en/latest/ref/cli/salt-call.html>。

- 在该 Minion 上执行高状态：

`salt-call state.highstate`

- 执行高状态的演练，计算所有更改但不实际执行：

`salt-call state.highstate test=true`

- 执行高状态并输出详细的调试信息：

`salt-call -l debug state.highstate`

- 列出该 Minion 的 Grains：

`salt-call grains.items`