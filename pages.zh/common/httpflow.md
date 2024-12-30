# httpflow

> 一款用于捕获和转储HTTP流的命令行工具。
> 更多信息请访问：<https://github.com/six-ddc/httpflow>。

- 在所有接口上捕获流量：

`httpflow -i {{any}}`

- 使用bpf样式的捕获来过滤结果：

`httpflow {{host httpbin.org or host baidu.com}}`

- 使用正则表达式根据URL过滤请求：

`httpflow -u '{{regular_expression}}'`

- 从PCAP格式的二进制文件中读取数据包：

`httpflow -r {{out.cap}}`

- 将输出写入目录：

`httpflow -w {{path/to/directory}}`