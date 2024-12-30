# salt-call

> 在一个 Salt 从属机上本地调用 Salt。
> 更多信息：<https://docs.saltproject.io/en/latest/ref/cli/salt-call.html>。

- 在此从属机上执行高状态：

`salt-call state.highstate`

- 执行高状态的干运行，计算所有更改但不实际执行它们：

`salt-call state.highstate test=true`

- 执行高状态并输出详细调试信息：

`salt-call -l debug state.highstate`

- 列出此从属机的 grains：

`salt-call grains.items`