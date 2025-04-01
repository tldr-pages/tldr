# grap

> 用于 groff（GNU Troff）文档格式系统的图表预处理器。
> 另请参阅 `pic` 和 `groff`。
> 更多信息：<https://manned.org/grap>。

- 处理一个 `grap` 文件，并将输出文件保存以供 `pic` 和 `groff` 后续处理：

`grap {{path/to/input.grap}} > {{path/to/output.pic}}`

- 使用 [me] 宏包将 `grap` 文件排版成 PDF，并将输出保存到文件中：

`grap {{path/to/input.grap}} | pic -T {{pdf}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`
