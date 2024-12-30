# 说

> 将文本转换为语音。
> 更多信息：<https://keith.github.io/xcode-man-pages/say.1.html>。

- 大声说出一个短语：

`say "{{我喜欢骑自行车。}}"`

- 大声朗读一个文件：

`say --input-file={{filename.txt}}`

- 用自定义的声音和语速说出一个短语：

`say --voice={{voice}} --rate={{每分钟单词数}} "{{对不起，Dave，我不能让你这么做。}}"`

- 列出可用的声音（不同的声音使用不同的语言）：

`say --voice="?"`

- 用波兰语说些什么：

`say --voice={{Zosia}} "{{Litwo, ojczyzno moja!}}"`

- 创建一个朗读文本的音频文件：

`say --output-file={{filename.aiff}} "{{为疯狂的人们干杯。}}"`