# ppmdraw

> 在 PPM 图像上通过执行脚本绘制线条、文本等。
> 有关使用的脚本语言的文档，请参见以下链接。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmdraw.html>。

- 通过执行提供的脚本在指定的 PPM 图像上绘制：

`ppmdraw -script '{{setpos 50 50; text_here "hello!"; }}' {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- 通过执行指定文件中的脚本在指定的 PPM 图像上绘制：

`ppmdraw -scriptfile {{path/to/script}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
