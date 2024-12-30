# exiv2

> 图像元数据处理工具。
> 更多信息请访问：<https://www.exiv2.org/manpage.html>。

- 打印图像 Exif 元数据的摘要：

`exiv2 {{path/to/file}}`

- 打印所有元数据（Exif、IPTC、XMP）及其解释值：

`exiv2 -P kt {{path/to/file}}`

- 打印所有元数据的原始值：

`exiv2 -P kv {{path/to/file}}`

- 从图像中删除所有元数据：

`exiv2 -d a {{path/to/file}}`

- 删除所有元数据，同时保留文件时间戳：

`exiv2 -d a -k {{path/to/file}}`

- 重命名文件，前缀为元数据中的日期和时间（而非文件时间戳）：

`exiv2 -r {{'%Y%m%d_%H%M%S_:basename:'}} {{path/to/file}}`