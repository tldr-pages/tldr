# pixterm

> 在终端中打印图像。
> 参见: `chafa`, `catimg`。
> 更多信息: <https://github.com/eliukblau/pixterm>。

- 在终端中直接渲染静态图像：

`pixterm {{path/to/file}}`

- 使用图像的原始宽高比：

`pixterm -s 2 {{path/to/file}}`

- 使用指定的终端行数和列数设置自定义宽高比：

`pixterm -tr {{24}} -tc {{80}} {{path/to/file}}`

- 使用带有 [m]atte 背景颜色和字符 [d]ithering 的输出过滤器：

`pixterm -m {{000000}} -d 2 {{path/to/file}}`
