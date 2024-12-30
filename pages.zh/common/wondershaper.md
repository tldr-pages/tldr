# wondershaper

> 允许用户限制网络适配器的带宽。
> 更多信息：<https://github.com/magnific0/wondershaper#usage>。

- 显示 [h]elp：

`wondershaper -h`

- 显示特定 [a]dapter 的当前 [s]tatus：

`wondershaper -s -a {{adapter_name}}`

- 清除特定 [a]dapter 的限制：

`wondershaper -c -a {{adapter_name}}`

- 设置特定的最大 [d]ownload 速率（单位：Kbps）：

`wondershaper -a {{adapter_name}} -d {{1024}}`

- 设置特定的最大 [u]pload 速率（单位：Kbps）：

`wondershaper -a {{adapter_name}} -u {{512}}`

- 设置特定的最大 [d]ownload 速率和 [u]pload 速率（单位：Kbps）：

`wondershaper -a {{adapter_name}} -d {{1024}} -u {{512}}`