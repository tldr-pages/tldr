# chafa

> 在终端中打印图像。
> 另见：`catimg`、`pixterm`。
> 更多信息：<https://hpjansson.org/chafa/man>。

- 直接在终端中渲染图像：

`chafa {{path/to/file}}`

- 使用 24 位 [c]olor 渲染图像：

`chafa -c full {{path/to/file}}`

- 使用抖动技术改善小调色板的图像渲染：

`chafa -c 16 --dither ordered {{path/to/file}}`

- 渲染图像，使其看起来像像素化：

`chafa --symbols vhalf {{path/to/file}}`

- 使用盲文字符渲染单色图像：

`chafa -c none --symbols braille {{path/to/file}}`