# grap

> 一个用于 groff（GNU Troff）文档排版系统的图表预处理器。
> 另见 `pic` 和 `groff`。
> 更多信息：<https://manned.org/grap>。

- 处理一个 `grap` 文件并保存输出文件，以便将来与 `pic` 和 `groff` 进行处理：

`grap {{path/to/input.grap}} > {{path/to/output.pic}}`

- 使用 [me] 宏包将 `grap` 文件排版为 PDF，并将输出保存到文件中：

`grap {{path/to/input.grap}} | pic -T {{pdf}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`