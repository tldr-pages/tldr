# mmdc

> 用于 mermaid 的命令行工具，mermaid 是一个使用领域特定语言生成图表的工具。
> 输入一个 mermaid 定义文件，输出一个 SVG、PNG 或 PDF 文件。
> 更多信息请访问：<https://mermaid-js.github.io/mermaid/>.

- 将文件转换为指定格式（根据文件扩展名自动确定）：

`mmdc --input {{input.mmd}} --output {{output.svg}}`

- 指定图表的主题：

`mmdc --input {{input.mmd}} --output {{output.svg}} --theme {{forest|dark|neutral|default}}`

- 指定图表的背景颜色（例如 `lime`、`"#D8064F"` 或 `transparent`）：

`mmdc --input {{input.mmd}} --output {{output.svg}} --backgroundColor {{color}}`