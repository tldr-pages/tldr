# httpflow

> 一个命令行工具，用于捕获和转储 HTTP 流。
> 更多信息：<https://github.com/six-ddc/httpflow>.

- 捕获所有接口上的流量：

`httpflow -i {{any}}`

- 使用 bpf 样式的捕获来过滤结果：

`httpflow {{host httpbin.org or host baidu.com}}`

- 使用正则表达式按 URL 过滤请求：

`httpflow -u '{{regular_expression}}'`

- 从 PCAP 格式的二进制文件中读取数据包：

`httpflow -r {{out.cap}}`

- 将输出写入目录：

`httpflow -w {{path/to/directory}}`
