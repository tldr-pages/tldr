# trans

> Translate Shell 是一个命令行翻译工具。
> 更多信息：<https://github.com/soimort/translate-shell>.

- 翻译一个单词（语言自动检测）：

`trans "{{word_or_sentence_to_translate}}"`

- 获取简短翻译：

`trans --brief "{{word_or_sentence_to_translate}}"`

- 将单词翻译成法语：

`trans :{{fr}} {{word}}`

- 将单词从德语翻译成英语：

`trans {{de}}:{{en}} {{Schmetterling}}`

- 作为词典使用，获取单词的含义：

`trans -d {{word}}`
