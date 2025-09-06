# alex

> 捕捉文本中的不敏感、不考虑他人的写作风格。它帮助您找出文本中的性别偏向、极端化、种族相关、宗教考虑不周等不平等表达。
> 更多信息：<https://github.com/get-alex/alex>.

- 从标准输入分析文本：

`echo {{His network looks good}} | alex --stdin`

- 分析当前目录中的所有文件：

`alex`

- 分析特定文件：

`alex {{路径/到/文件.md}}`

- 分析除了 `示例文件.md` 之外的所有 Markdown 文件：

`alex *.md !{{示例文件.md}}`
