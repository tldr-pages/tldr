# cpufreq-aperf

> 计算特定时间段内的平均 CPU 频率。
> 需要 root 权限。
> 更多信息：<https://manned.org/cpufreq-aperf>.

- 开始计算，默认为所有 CPU 核心，刷新间隔 1 秒：

`sudo cpufreq-aperf`

- 只为 CPU 1 开始计算：

`sudo cpufreq-aperf -c {{1}}`

- 为所有 CPU 核心设置 3 秒刷新间隔开始计算：

`sudo cpufreq-aperf -i {{3}}`

- 只计算一次：

`sudo cpufreq-aperf -o`
