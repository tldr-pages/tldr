# cpupower

> 有关 CPU 功耗和调优选项的工具。
> 更多信息：<https://manned.org/cpupower>.

- 列出所有 CPU：

`sudo cpupower {{[-c|--cpu]}} {{all}} info`

- 打印所有核心的信息：

`sudo cpupower {{[-c|--cpu]}} {{all}} info`

- 将所有 CPU 设置为节能频率策略：

`sudo cpupower {{[-c|--cpu]}} {{all}} frequency-set --governor {{powersave}}`

- 打印 CPU 0 的可用频率策略：

`sudo cpupower {{[-c|--cpu]}} {{0}} frequency-info {{[-g|--governors]}} | grep "analyzing\|governors"`

- 以人类可读的格式打印 CPU 4 的硬件频率：

`sudo cpupower {{[-c|--cpu]}} {{4}} frequency-info {{[-w|--hwfreq]}} {{[-m|--human]}}`
