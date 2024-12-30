# Snort

> 开源网络入侵检测系统。
> 更多信息：<https://www.snort.org/#documents>。

- 捕获数据包并输出详细信息：

`sudo snort -v -i {{interface}}`

- 捕获数据包并转储应用层数据，输出详细信息：

`sudo snort -vd -i {{interface}}`

- 捕获数据包并显示链路层数据包头，输出详细信息：

`sudo snort -ve -i {{interface}}`

- 捕获数据包并将其保存在指定目录中：

`sudo snort -i {{interface}} -l {{path/to/directory}}`

- 根据规则捕获数据包并保存有问题的数据包和警报：

`sudo snort -i {{interface}} -c {{path/to/rules.conf}} -l {{path/to/directory}}`