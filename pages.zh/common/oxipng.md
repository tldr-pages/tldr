# oxipng

> 无损改善 PNG 文件的压缩。
> 更多信息：<https://github.com/shssoichiro/oxipng>。

- 压缩一个 PNG 文件（默认情况下覆盖该文件）：

`oxipng {{path/to/file.png}}`

- 压缩一个 PNG 文件并将输出保存到新文件：

`oxipng --out {{path/to/output.png}} {{path/to/file.png}}`

- 使用多线程压缩当前目录中的所有 PNG 文件：

`oxipng "*.png"`

- 使用设定的优化级别压缩文件（默认级别为 2）：

`oxipng --opt {{0|1|2|3|4|5|6|max}} {{path/to/file.png}}`

- 设置 PNG 交错类型（`0` 移除交错，`1` 应用 Adam7 交错，`keep` 保留现有交错；默认值为 `0`）：

`oxipng --interlace {{0|1|keep}} {{path/to/file.png}}`

- 对具有 alpha 通道的图像进行额外优化：

`oxipng --alpha {{path/to/file.png}}`

- 使用更慢但更强的 Zopfli 压缩器，进行最大优化：

`oxipng --zopfli --opt max {{path/to/file.png}}`

- 去除所有非关键元数据块：

`oxipng --strip all {{path/to/file.png}}`