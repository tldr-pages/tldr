# 转换

> Translate Shell 是一个命令行翻译工具。
> 更多信息：<https://github.com/soimort/translate-shell>。

- 翻译一个单词（语言自动检测）：

`trans "{{要翻译的单词或句子}}"`

- 获取简短翻译：

`trans --brief "{{要翻译的单词或句子}}"`

- 将单词翻译成法语：

`trans :{{fr}} {{单词}}`

- 将德语单词翻译成英语：

`trans {{de}}:{{en}} {{Schmetterling}}`

- 像字典一样获取单词的意思：

`trans -d {{单词}}`