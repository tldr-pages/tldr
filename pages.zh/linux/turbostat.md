# turbostat

> 报告处理器拓扑、频率、温度、功率和空闲统计信息。
> 更多信息：<https://manned.org/turbostat.8>。

- 每5秒显示一次统计信息：

`sudo turbostat`

- 每指定的秒数显示一次统计信息：

`sudo turbostat -i {{n_seconds}}`

- 不解码并打印系统配置头信息：

`sudo turbostat --quiet`

- 每1秒显示有关CPU的有用信息，不包括头信息：

`sudo turbostat --quiet --interval 1 --cpu 0-{{CPU_thread_count}} --show "PkgWatt","Busy%","Core","CoreTmp","Thermal"`

- 显示帮助信息：

`turbostat --help`