# pngquant

> PNG 转换器和有损图片压缩工具。
> 更多信息：<https://pngquant.org/>。

- 尽可能压缩特定的 PNG 文件，并将结果写入新文件：

`pngquant {{path/to/file.png}}`

- 压缩特定的 PNG 文件并覆盖原文件：

`pngquant --ext .png --force {{path/to/file.png}}`

- 尝试以自定义质量压缩特定的 PNG 文件（如果低于最小值则跳过）：

`pngquant --quality {{0-100}} {{path/to/file.png}}`

- 压缩特定的 PNG 文件并将颜色数减少到 64：

`pngquant {{64}} {{path/to/file.png}}`

- 压缩特定的 PNG 文件，如果压缩后的文件大于原文件则跳过：

`pngquant --skip-if-larger {{path/to/file.png}}`

- 压缩特定的 PNG 文件并删除元数据：

`pngquant --strip {{path/to/file.png}}`

- 压缩特定的 PNG 文件并保存到指定路径：

`pngquant {{path/to/file.png}} --output {{path/to/file.png}}`

- 压缩特定的 PNG 文件并显示进度：

`pngquant --verbose {{path/to/file.png}}`