# mitmdump

> 查看、记录并编程转换 HTTP 流量。
> 作为 mitmproxy 的命令行版本。
> 更多信息：<https://docs.mitmproxy.org/stable/#mitmdump>。

- 启动代理并将所有输出保存到文件：

`mitmdump -w {{path/to/file}}`

- 从已保存的流量文件中过滤出仅包含 POST 请求：

`mitmdump -nr {{input_filename}} -w {{output_filename}} "{{~m post}}"`

- 重放已保存的流量文件：

`mitmdump -nc {{path/to/file}}`