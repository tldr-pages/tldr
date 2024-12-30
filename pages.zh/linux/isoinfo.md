# isoinfo

> 用于转储和验证ISO磁盘映像的实用程序。
> 更多信息：<https://manned.org/isoinfo>。

- 列出ISO映像中包含的所有文件：

`isoinfo -f -i {{path/to/image.iso}}`

- 提取ISO映像中的特定文件并将其输出到`stdout`：

`isoinfo -i {{path/to/image.iso}} -x {{/PATH/TO/FILE/INSIDE/ISO.EXT}}`

- 显示ISO磁盘映像的头信息：

`isoinfo -d -i {{path/to/image.iso}}`