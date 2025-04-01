# pw-link

> 管理 PipeWire 中端口之间的链接。
> 更多信息：<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- 列出所有音频输出和输入端口及其ID：

`pw-link {{[-oiI|--output --input --ids]}}`

- 在输出端口和输入端口之间创建链接：

`pw-link {{output_port_name}} {{input_port_name}}`

- 断开两个端口的链接：

`pw-link {{[-d|--disconnect]}} {{output_port_name}} {{input_port_name}}`

- 列出所有链接及其ID：

`pw-link {{[-lI|--links --ids]}}`

- 显示帮助：

`pw-link {{[-h|--help]}}`
