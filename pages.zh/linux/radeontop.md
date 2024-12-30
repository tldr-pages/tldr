# radeontop

> 显示 AMD GPU 的利用率。
> 可能需要根据您的系统获得根权限。
> 更多信息：<https://github.com/clbr/radeontop>。

- 显示默认 AMD GPU 的利用率：

`radeontop`

- 启用彩色输出：

`radeontop --color`

- 选择特定的 GPU（总线编号是 `lspci` 输出中的第一个数字）：

`radeontop --bus {{bus_number}}`

- 指定显示刷新率（更高意味着更多 GPU 开销）：

`radeontop --ticks {{samples_per_second}}`