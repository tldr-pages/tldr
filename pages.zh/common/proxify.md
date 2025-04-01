# proxify

> 一个便携且多功能的代理工具，用于捕获、操作和重放HTTP/HTTPS流量。
> 参见：`mitmproxy`。
> 更多信息：<https://github.com/projectdiscovery/proxify>。

- 启动HTTP代理（在回环网络接口 `127.0.0.1` 和端口 `8888` 上）：

`proxify`

- 在自定义网络接口和端口上启动HTTP代理（端口号低于 `1024` 时可能需要 `sudo`）：

`proxify -http-addr "{{ip_address}}:{{port_number}}"`

- 指定输出格式和输出文件：

`proxify -output-format {{jsonl|yaml}} -output {{path/to/file}}`

- 显示帮助：

`proxify -h`