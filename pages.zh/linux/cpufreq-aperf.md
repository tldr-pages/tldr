# cpufreq-aperf

> 计算一段时间内的平均 CPU 频率。
> 需要 root 权限。
> 更多信息：<https://manned.org/cpufreq-aperf>。

- 开始计算，默认针对所有 CPU 核心和 1 秒刷新间隔：

`sudo cpufreq-aperf`

- 仅针对 CPU 1 开始计算：

`sudo cpufreq-aperf -c {{1}}`

- 针对所有 CPU 核心以 3 秒刷新间隔开始计算：

`sudo cpufreq-aperf -i {{3}}`

- 仅计算一次：

`sudo cpufreq-aperf -o`