# cpufreq-info

> 显示 CPU 频率信息。
> 更多信息：<https://manned.org/cpufreq-info>。

- 显示所有 CPU 的频率信息：

`cpufreq-info`

- 显示指定 CPU 的频率信息：

`cpufreq-info -c {{cpu_number}}`

- 显示允许的最小和最大 CPU 频率：

`cpufreq-info -l`

- 以表格格式显示当前的最小和最大 CPU 频率及政策：

`cpufreq-info -o`

- 显示可用的 CPU 频率政策：

`cpufreq-info -g`

- 根据 cpufreq 内核模块，以人类可读的格式显示当前 CPU 工作频率：

`cpufreq-info -f -m`

- 通过从硬件读取当前 CPU 工作频率，以人类可读的格式显示（仅对 root 可用）：

`sudo cpufreq-info -w -m`