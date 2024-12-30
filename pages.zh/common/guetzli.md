# guetzli

> JPEG图像压缩工具。
> 更多信息：<https://github.com/google/guetzli>。

- 压缩JPEG图像：

`guetzli {{input.jpg}} {{output.jpg}}`

- 从PNG创建压缩的JPEG：

`guetzli {{input.png}} {{output.jpg}}`

- 使用所需的视觉质量压缩JPEG（84-100）：

`guetzli --quality {{quality_value}} {{input.jpg}} {{output.jpg}}`