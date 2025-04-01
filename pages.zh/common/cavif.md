# cavif

> 将 PNG/JPEG 图像转换为 AVIF。使用 Rust 编写。
> 另见: `convert`。
> 更多信息: <https://github.com/kornelski/cavif-rs>.

- 将 JPEG 文件转换为 AVIF，保存为 `file.avif`：

`cavif {{path/to/image.jpg}}`

- 调整图像质量并转换 PNG 文件为 AVIF：

`cavif --quality {{1..100}} {{path/to/image.png}}`

- 指定输出位置：

`cavif {{path/to/image.jpg}} --output {{path/to/output.avif}}`

- 如果目标文件已存在，则覆盖该文件：

`cavif --overwrite {{path/to/image.jpg}}`