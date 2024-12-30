# zlib-flate

> 原始 zlib 压缩和解压缩程序。
> 是 `qpdf` 的一部分。
> 更多信息请访问: <https://manned.org/zlib-flate>。

- 压缩文件：

`zlib-flate -compress < {{path/to/input_file}} > {{path/to/compressed.zlib}}`

- 解压缩文件：

`zlib-flate -uncompress < {{path/to/compressed.zlib}} > {{path/to/output_file}}`

- 使用指定的压缩级别压缩文件。0=最快（最差），9=最慢（最好）：

`zlib-flate -compress={{compression_level}} < {{path/to/input_file}} > {{path/to/compressed.zlib}}`