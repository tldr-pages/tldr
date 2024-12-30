# cpufreq-set

> 一个用于修改CPU频率设置的工具。
> 频率值应在命令 `cpufreq-info -l` 的输出范围内。
> 更多信息：<https://manned.org/cpufreq-set>。

- 将CPU 1的CPU频率策略设置为“用户空间”：

`sudo cpufreq-set -c {{1}} -g {{userspace}}`

- 设置CPU 1的当前最小CPU频率：

`sudo cpufreq-set -c {{1}} --min {{min_frequency}}`

- 设置CPU 1的当前最大CPU频率：

`sudo cpufreq-set -c {{1}} --max {{max_frequency}}`

- 设置CPU 1的当前工作频率：

`sudo cpufreq-set -c {{1}} -f {{work_frequency}}`