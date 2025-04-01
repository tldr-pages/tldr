# texcount

> 统计 TeX 文档中的单词，忽略宏。
> 注意：如果 TeX 文档使用了 `\include` 或 `\input`，并且您希望统计被包含的文件，`texcount` 必须在根 TeX 文件所在的目录中运行。
> 更多信息：<https://app.uio.no/ifi/texcount/howto.html>。

- 统计 TeX 文件中的单词：

`texcount {{path/to/file.tex}}`

- 统计主文档和通过 `\input` 或 `\include` 包含的子文档中的单词：

`texcount -merge {{file.tex}}`

- 统计主文档和子文档中的单词，分别列出每个文件的单词数（以及总数）：

`texcount -inc {{file.tex}}`

- 统计主文档和子文档中的单词，并按章节（而不是小节）分组统计：

`texcount -merge -sub=chapter {{file.tex}}`

- 统计单词并输出详细信息：

`texcount -v {{path/to/file.tex}}`
