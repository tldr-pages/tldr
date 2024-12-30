# plantuml

> 从纯文本语言创建 UML 图，并以不同格式呈现它们。
> 更多信息：<https://plantuml.com/zh/command-line>。

- 将图渲染为默认格式（PNG）：

`plantuml {{diagram1.puml}} {{diagram2.puml}}`

- 将图以给定格式渲染（例如 `png`、`pdf`、`svg`、`txt`）：

`plantuml -t {{format}} {{diagram.puml}}`

- 渲染一个目录下的所有图：

`plantuml {{path/to/diagrams}}`

- 将图渲染到输出目录：

`plantuml -o {{path/to/output}} {{diagram.puml}}`

- 渲染图而不存储图的源代码（注意：当未指定 `-nometadata` 选项时，默认会存储）：

`plantuml -nometadata {{diagram.png}} > {{diagram.puml}}`

- 从 `plantuml` 图的元数据中检索源代码：

`plantuml -metadata {{diagram.png}} > {{diagram.puml}}`

- 使用配置文件渲染图：

`plantuml -config {{config.cfg}} {{diagram.puml}}`

- 显示帮助信息：

`plantuml -help`