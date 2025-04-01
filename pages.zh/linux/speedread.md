# speedread

> 一个简单的基于终端的开源 Spritz 类应用程序。
> 通过在最佳阅读点上按单词显示输入文本（快速串行视觉呈现，RSVP），使眼睛可以固定在一个位置，实现比平常更快的阅读速度。
> 更多信息：<https://github.com/pasky/speedread>.

- 以特定速度阅读文本文件：

`cat {{path/to/file.txt}} | speedread -wpm {{250}}`

- 从特定行继续阅读：

`cat {{path/to/file.txt}} | speedread -resume {{5}}`

- 一次显示多个单词：

`cat {{path/to/file.txt}} | speedread -multiword`

- 在阅读会话中减速 10%：

`<[>`

- 在阅读会话中加速 10%：

`<]>`

- 暂停，并显示最后几行作为上下文：

`<Space>`
