# say

> 将文本转换为语音。
> 更多信息：<https://ss64.com/osx/say.html>.

- 大声说出一个句子：

`say "{{我喜欢骑脚踏车。}}"`

- 播放文本文件内容音频：

`say --input-file={{文件名.txt}}`

- 用自定义的语音和语音速率说出一个句子：

`say --voice={{语音库名}} --rate={{每分钟多少词}} "{{戴夫，我很抱歉，我不能让你那么干。}}"`

- 列出可用的语音库（不同的语音用于不同的语言）：

`say --voice="?"`

- 用波兰语说一个句子：

`say --voice={{Zosia}} "{{Litwo, ojczyzno moja!}}"`

- 创建文本的音频文件：

`say --output-file={{文件名.aiff}} "{{献给疯狂的人们。}}"`
