# pw-dot

> 生成 PipeWire 图的 `.dot` 文件。
> 参见：`dot`，用于渲染图。
> 更多信息：<https://docs.pipewire.org/page_man_pw-dot_1.html>。

- 生成图并保存到 `pw.dot` 文件：

`pw-dot`

- 从 `pw-dump` JSON 文件读取对象：

`pw-dot {{[-j|--json]}} {{path/to/file.json}}`

- 指定输出文件，显示所有对象类型：

`pw-dot {{[-o|--output]}} {{path/to/file.dot}} {{[-a|--all]}}`

- 将 `.dot` 图打印到 `stdout`，显示所有对象属性：

`pw-dot {{[-o|--output]}} - {{[-d|--detail]}}`

- 从远程实例生成图，仅显示已连接的对象：

`pw-dot {{[-r|--remote]}} {{remote_name}} {{[-s|--smart]}}`

- 从左到右布局图，而不是从上到下：

`pw-dot {{[-L|--lr]}}`

- 使用 90 度角布局图中的边：

`pw-dot {{[-9|--90]}}`

- 显示帮助：

`pw-dot {{[-h|--help]}}`