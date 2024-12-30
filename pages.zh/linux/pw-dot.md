# pw-dot

> 创建 PipeWire 图的 `.dot` 文件。
> 另见：`dot`，用于渲染图。
> 更多信息：<https://docs.pipewire.org/page_man_pw-dot_1.html>。

- 生成一个图到 `pw.dot` 文件：

`pw-dot`

- 从 `pw-dump` JSON 文件中读取对象：

`pw-dot {{-j|--json}} {{path/to/file.json}}`

- 指定一个 [o]utput 文件，显示所有对象类型：

`pw-dot --output {{path/to/file.dot}} {{-a|--all}}`

- 将 `.dot` 图打印到 `stdout`，显示所有对象属性：

`pw-dot --output - {{-d|--detail}}`

- 从 [r]emote 实例生成图，仅显示链接的对象：

`pw-dot --remote {{remote_name}} {{-s|--smart}}`

- 使图从左到右布局，而不是 dot 的默认从上到下：

`pw-dot {{-L|--lr}}`

- 使用 90 度角的边缘布局图：

`pw-dot {{-9|--90}}`

- 显示帮助信息：

`pw-dot --help`