# wondershaper

> 允许用户限制网络适配器的带宽。
> 更多信息：<https://github.com/magnific0/wondershaper#usage>.

- 显示帮助信息：

`wondershaper -h`

- 显示特定适配器的当前状态：

`wondershaper -s -a {{adapter_name}}`

- 清除特定适配器的限制：

`wondershaper -c -a {{adapter_name}}`

- 设置特定的最大下载速率（单位：Kbps）：

`wondershaper -a {{adapter_name}} -d {{1024}}`

- 设置特定的最大上传速率（单位：Kbps）：

`wondershaper -a {{adapter_name}} -u {{512}}`

- 设置特定的最大下载速率和上传速率（单位：Kbps）：

`wondershaper -a {{adapter_name}} -d {{1024}} -u {{512}}`