# cpupower

> 关于 CPU 电源和调节选项的工具。
> 更多信息：<https://manned.org/cpupower>。

- 列出所有 CPU：

`sudo cpupower --cpu {{all}} info`

- 打印所有核心的信息：

`sudo cpupower --cpu {{all}} info`

- 将所有 CPU 设置为节能频率调节器：

`sudo cpupower --cpu {{all}} frequency-set --governor {{powersave}}`

- 打印 CPU 0 可用的频率 [g]overnors：

`sudo cpupower --cpu {{0}} frequency-info g | grep "analyzing\|governors"`

- 以人类可读的格式打印 CPU 4 的硬件频率：

`sudo cpupower --cpu {{4}} frequency-info --hwfreq --human`