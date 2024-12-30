# mitmdump

> 查看、记录并以编程方式转换 HTTP 流量。
> mitmproxy 的命令行版本。
> 更多信息：<https://docs.mitmproxy.org/stable/#mitmdump>。

- 启动代理并将所有输出保存到文件中：

`mitmdump -w {{path/to/file}}`

- 过滤保存的流量文件，仅保留 POST 请求：

`mitmdump -nr {{input_filename}} -w {{output_filename}} "{{~m post}}"`

- 重播保存的流量文件：

`mitmdump -nc {{path/to/file}}`