# 快速阅读

> 一个简单的基于终端的开源Spritz类工具。
> 以每个单词的快速序列视觉呈现（RSVP）形式显示输入文本，按照最佳阅读点对齐，使得阅读文本的速度远快于平常，因为眼睛可以固定在一个地方。
> 更多信息：<https://github.com/pasky/speedread>。

- 以特定速度读取文本文件：

`cat {{path/to/file.txt}} | speedread -wpm {{250}}`

- 从特定行恢复：

`cat {{path/to/file.txt}} | speedread -resume {{5}}`

- 同时显示多个单词：

`cat {{path/to/file.txt}} | speedread -multiword`

- 在阅读过程中减慢10%的速度：

`[`

- 在阅读过程中加快10%的速度：

`]`

- 暂停，并显示最后几行作为上下文：

`<space>`