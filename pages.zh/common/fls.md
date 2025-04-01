# fls

> 列出映像文件或设备中的文件和目录。
> 更多信息：<https://wiki.sleuthkit.org/index.php?title=Fls>。

- 在设备上构建递归的 fls 列表，输出路径将以 C: 开头：

`fls -r -m {{C:}} {{/dev/loop1p1}}`

- 分析单个分区，提供文件系统在映像中开始的扇区偏移量：

`fls -r -m {{C:}} -o {{sector}} {{path/to/image_file}}`

- 分析单个分区，提供原始系统的时区：

`fls -r -m {{C:}} -z {{timezone}} {{/dev/loop1p1}}`
