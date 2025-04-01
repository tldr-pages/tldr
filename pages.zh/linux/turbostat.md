# turbostat

> 报告处理器拓扑、频率、温度、功耗和空闲统计信息。
> 更多信息：https://manned.org/turbostat.8.

- 每 5 秒显示一次统计信息：

`sudo turbostat`

- 每隔指定的秒数显示一次统计信息：

`sudo turbostat -i {{n_seconds}}`

- 不解码并打印系统配置头部信息：

`sudo turbostat --quiet`

- 每 1 秒显示关于 CPU 的有用信息，不包含头部信息：

`sudo turbostat --quiet --interval 1 --cpu 0-{{CPU线程数}} --show "PkgWatt","Busy%","Core","CoreTmp","Thermal"`

- 显示帮助信息：

`turbostat --help`