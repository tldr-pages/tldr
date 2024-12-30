# sysdig

> 系统故障排除、分析和探索。
> 捕获、过滤和存储系统调用。
> 更多信息：<https://github.com/draios/sysdig/wiki>。

- 捕获来自实时系统的所有事件并打印到屏幕：

`sysdig`

- 捕获来自实时系统的所有事件并保存到磁盘：

`sysdig -w {{path/to/file}}.scap`

- 从文件中读取事件并打印到屏幕：

`sysdig -r {{path/to/file}}.scap`

- 过滤并打印由 cat 调用的所有打开的系统调用：

`sysdig proc.name=cat and evt.type=open`

- 注册任何找到的插件，并使用 dummy 作为输入源，传递打开参数：

`sysdig -I dummy:'{{parameter}}'`

- 列出可用的 chisels：

`sysdig -cl`

- 使用 spy_ip chisel 查看与 IP 地址交换的数据：

`sysdig -c spy_ip {{ip_address}}`