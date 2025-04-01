# pw-dump

> 以 JSON 格式转储 PipeWire 的当前状态，包括节点、设备、模块、端口等信息。
> 参见：`pw-mon`。
> 更多信息：<https://docs.pipewire.org/page_man_pw-dump_1.html>。

- 打印默认 PipeWire 实例的当前状态的 JSON 表示：

`pw-dump`

- 打印指定对象的 JSON 表示：

`pw-dump {{object_id}}`

- 转储当前状态并监视更改，再次打印：

`pw-dump {{[-m|--monitor]}}`

- 将远程实例的当前状态转储到文件中：

`pw-dump {{[-r|--remote]}} {{remote_name}} > {{path/to/dump_file.json}}`

- 设置颜色配置：

`pw-dump {{[-C|--color]}} {{never|always|auto}}`

- 显示帮助信息：

`pw-dump {{[-h|--help]}}`