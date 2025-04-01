# ect

> 高效压缩工具。
> 使用 C++ 编写的文件优化器，支持 PNG、JPEG、gzip 和 Zip 文件。
> 更多信息：<https://github.com/fhanau/Efficient-Compression-Tool>.

- 压缩文件：

`ect {{path/to/file.png}}`

- 使用指定的压缩级别和多线程压缩文件（1=最快（最差），9=最慢（最好），默认为 3）：

`ect -{{9}} --mt-deflate {{path/to/file.zip}}`

- 递归压缩目录中的所有文件：

`ect -recurse {{path/to/directory}}`

- 压缩文件，保留原始修改时间：

`ect -keep {{path/to/file.png}}`

- 压缩文件，移除元数据：

`ect -strip {{path/to/file.png}}`
