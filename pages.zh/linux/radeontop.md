# radeontop

> 显示 AMD GPU 的利用率。
> 根据系统不同，可能需要 root 权限。
> 更多信息：<https://github.com/clbr/radeontop>.

- 显示默认 AMD GPU 的利用率：

`radeontop`

- 启用彩色输出：

`radeontop --color`

- 选择特定的 GPU（总线号是 `lspci` 命令输出中的第一个数字）：

`radeontop --bus {{bus_number}}`

- 指定显示刷新率（数值越高意味着更多的 GPU 开销）：

`radeontop --ticks {{samples_per_second}}`
