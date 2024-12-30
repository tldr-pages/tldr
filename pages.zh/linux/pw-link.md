# pw-link

> 管理 PipeWire 中端口之间的链接。
> 更多信息：<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>。

- 列出所有音频输出和输入端口及其 ID：

`pw-link --output --input --ids`

- 在一个输出端口和一个输入端口之间创建链接：

`pw-link {{output_port_name}} {{input_port_name}}`

- 断开两个端口的连接：

`pw-link --disconnect {{output_port_name}} {{input_port_name}}`

- 列出所有链接及其 ID：

`pw-link --links --ids`

- 显示帮助信息：

`pw-link -h`