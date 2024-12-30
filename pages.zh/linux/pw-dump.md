# pw-dump

> 以 JSON 格式转储 PipeWire 的当前状态，包括节点、设备、模块、端口和其他对象的信息。
> 另见：`pw-mon`。
> 更多信息：<https://docs.pipewire.org/page_man_pw-dump_1.html>。

- 打印默认 PipeWire 实例当前状态的 JSON 表示：

`pw-dump`

- 转储当前状态并 [监]控变化，再次打印出来：

`pw-dump --monitor`

- 将 [远]程实例的当前状态转储到文件：

`pw-dump --remote {{remote_name}} > {{path/to/dump_file.json}}`

- 设置 [颜]色配置：

`pw-dump --color {{never|always|auto}}`

- 显示帮助：

`pw-dump --help`