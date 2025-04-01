# exiv2

> 图像元数据操作工具。
> 更多信息：<https://www.exiv2.org/manpage.html>。

- 打印图像的 Exif 元数据摘要：

`exiv2 {{path/to/file}}`

- 打印所有元数据（Exif、IPTC、XMP）并显示解释后的值：

`exiv2 -P kt {{path/to/file}}`

- 打印所有元数据的原始值：

`exiv2 -P kv {{path/to/file}}`

- 从图像中删除所有元数据：

`exiv2 -d a {{path/to/file}}`

- 删除所有元数据，同时保留文件的时间戳：

`exiv2 -d a -k {{path/to/file}}`

- 根据元数据（而非文件的时间戳）中的日期和时间重命名文件：

`exiv2 -r {{'%Y%m%d_%H%M%S_:basename:'}} {{path/to/file}}`