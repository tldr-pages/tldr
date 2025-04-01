# chafa

> 在终端中打印图像。
> 参见：`catimg`、`pixterm`。
> 更多信息：<https://hpjansson.org/chafa/man>。

- 直接在终端中渲染图像：

`chafa {{path/to/file}}`

- 使用 24 位颜色渲染图像：

`chafa {{[-c|--colors]}} full {{path/to/file}}`

- 使用抖动技术改善小色板的图像渲染效果：

`chafa {{[-c|--colors]}} 16 --dither ordered {{path/to/file}}`

- 渲染图像，使其看起来像素化：

`chafa --symbols vhalf {{path/to/file}}`

- 使用只有盲文字符渲染黑白图像：

`chafa {{[-c|--colors]}} none --symbols braille {{path/to/file}}`