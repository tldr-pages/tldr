# oxipng

> 无损地优化 PNG 文件的压缩。
> 更多信息：<https://github.com/shssoichiro/oxipng>.

- 压缩一个 PNG 文件（默认情况下覆盖原文件）：

`oxipng {{path/to/file.png}}`

- 压缩一个 PNG 文件并保存输出到新文件：

`oxipng --out {{path/to/output.png}} {{path/to/file.png}}`

- 使用多线程压缩当前目录中的所有 PNG 文件：

`oxipng "*.png"`

- 用指定的优化级别压缩文件（默认为 2）：

`oxipng --opt {{0|1|2|3|4|5|6|max}} {{path/to/file.png}}`

- 设置 PNG 图像的交错类型（`0` 为取消交错，`1` 为使用 Adam7 交错，`keep` 为保留现有交错；默认为 `0`）：

`oxipng --interlace {{0|1|keep}} {{path/to/file.png}}`

- 对带有 alpha 通道的图像进行额外优化：

`oxipng --alpha {{path/to/file.png}}`

- 使用速度较慢但压缩效果更强的 Zopfli 压缩器进行最大优化：

`oxipng --zopfli --opt max {{path/to/file.png}}`

- 删除所有非关键的元数据块：

`oxipng --strip all {{path/to/file.png}}`