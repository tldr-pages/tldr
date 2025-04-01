# snort

> 开源网络入侵检测系统。
> 更多信息：<https://www.snort.org/#documents>.

- 以详细模式捕获数据包：

`sudo snort -v -i {{interface}}`

- 以详细模式捕获数据包并转储应用层数据：

`sudo snort -vd -i {{interface}}`

- 以详细模式捕获数据包并显示链路层数据包头部信息：

`sudo snort -ve -i {{interface}}`

- 捕获数据包并保存到指定目录：

`sudo snort -i {{interface}} -l {{path/to/directory}}`

- 根据规则捕获数据包，并保存违规的数据包和警报：

`sudo snort -i {{interface}} -c {{path/to/rules.conf}} -l {{path/to/directory}}`
