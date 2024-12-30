# texcount

> 计算 TeX 文档中的单词数量，忽略宏。
> 注意：如果 TeX 文档使用 `\include` 或 `\input`，并且您想要计算包含的文件，则必须在根 TeX 文件的目录中运行 `texcount`。
> 更多信息：<https://app.uio.no/ifi/texcount/howto.html>。

- 计算 TeX 文件中的单词数：

`texcount {{path/to/file.tex}}`

- 计算文档及其通过 `\input` 或 `\include` 引入的子文档中的单词数：

`texcount -merge {{file.tex}}`

- 计算文档及其子文档中的单词数，分别列出每个文件（以及总计数）：

`texcount -inc {{file.tex}}`

- 计算文档及其子文档中的单词数，按章节（而不是小节）进行子计数：

`texcount -merge -sub=chapter {{file.tex}}`

- 计算单词并输出详细信息：

`texcount -v {{path/to/file.tex}}`