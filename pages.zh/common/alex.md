# alex

> 捕捉不敏感、不体贴的写作。
> 它帮助你在文本中找到性别偏见、极化、与种族相关、宗教不体贴或其他不平等的措辞。
> 更多信息：<https://github.com/get-alex/alex>。

- 从 `stdin` 分析文本：

`echo {{他的网络看起来不错}} | alex --stdin`

- 分析当前目录中的所有文件：

`alex`

- 分析特定文件：

`alex {{path/to/file.md}}`

- 分析所有 Markdown 文件，除了 `example.md`：

`alex *.md !{{example.md}}`