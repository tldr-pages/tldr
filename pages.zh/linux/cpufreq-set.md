# cpufreq-set

> 用于修改 CPU 频率设置的工具。
> 频率值应在 `cpufreq-info -l` 命令输出的范围内。
> 更多信息：<https://manned.org/cpufreq-set>。

- 将 CPU 1 的 CPU 频率策略设置为 "userspace"：

`sudo cpufreq-set -c {{1}} -g {{userspace}}`

- 设置 CPU 1 的当前最小 CPU 频率：

`sudo cpufreq-set -c {{1}} --min {{min_frequency}}`

- 设置 CPU 1 的当前最大 CPU 频率：

`sudo cpufreq-set -c {{1}} --max {{max_frequency}}`

- 设置 CPU 1 的当前工作频率：

`sudo cpufreq-set -c {{1}} -f {{work_frequency}}`