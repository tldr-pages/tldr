# mmdc

> Mermaid 的命令行工具，Mermaid 是一种使用领域特定语言生成图表的工具。
> 输入一个 Mermaid 定义文件，输出为 SVG、PNG 或 PDF 文件。
> 更多信息：<https://mermaid-js.github.io/mermaid/>。

- 将文件转换为指定格式（格式由文件扩展名自动确定）：

`mmdc --input {{input.mmd}} --output {{output.svg}}`

- 指定图表的主题：

`mmdc --input {{input.mmd}} --output {{output.svg}} --theme {{forest|dark|neutral|default}}`

- 指定图表的背景色（例如 `lime`，`"#D8064F"`，或 `transparent`）：

`mmdc --input {{input.mmd}} --output {{output.svg}} --backgroundColor {{color}}`