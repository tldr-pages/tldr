# plantuml

> 使用纯文本语言创建 UML 图表并将其渲染为不同的格式。
> 更多信息：<https://plantuml.com/en/command-line>.

- 以默认格式（PNG）渲染图表：

`plantuml {{diagram1.puml}} {{diagram2.puml}}`

- 以指定格式（如 `png`、`pdf`、`svg`、`txt`）渲染图表：

`plantuml -t {{format}} {{diagram.puml}}`

- 渲染指定目录中的所有图表：

`plantuml {{path/to/diagrams}}`

- 将图表渲染到输出目录：

`plantuml -o {{path/to/output}} {{diagram.puml}}`

- 渲染图表但不存储图表的源代码（注意：如果不指定 `-nometadata` 选项，默认会存储源代码）：

`plantuml -nometadata {{diagram.png}} > {{diagram.puml}}`

- 从 `plantuml` 图表的元数据中检索源代码：

`plantuml -metadata {{diagram.png}} > {{diagram.puml}}`

- 使用配置文件渲染图表：

`plantuml -config {{config.cfg}} {{diagram.puml}}`

- 显示帮助：

`plantuml -help`
