# guetzli

> JPEG 图像压缩工具。
> 更多信息：<https://github.com/google/guetzli>.

- 压缩 JPEG 图像：

`guetzli {{input.jpg}} {{output.jpg}}`

- 从 PNG 创建压缩的 JPEG：

`guetzli {{input.png}} {{output.jpg}}`

- 以所需的视觉质量（84-100）压缩 JPEG：

`guetzli --quality {{quality_value}} {{input.jpg}} {{output.jpg}}`
